#!/usr/bin/env python3
"""
Parse AME 2020 atomic mass data to extract nuclear binding energies
and look for gaps/shells in the data
"""

import numpy as np
import re
from collections import defaultdict

def parse_ame2020(filename):
    """
    Parse AME 2020 mass file
    
    Format (from header):
    cc NZ  N  Z  A    el  o     mass  unc binding unc      B  beta  unc    atomic_mass   unc
    
    Returns:
        list of dicts with nuclear data
    """
    nuclides = []
    
    with open(filename, 'r') as f:
        for line in f:
            # Skip header lines and short lines
            if len(line) < 100:
                continue
            # Data lines start with spaces and numbers, skip lines starting with 0 or 1 (page/line feed)
            if line[0] in ['0', '1']:
                continue
                
            try:
                # Parse fixed-width format
                nz = int(line[0:4])
                N = int(line[4:9])
                Z = int(line[9:14])
                A = int(line[14:19])
                el = line[20:23].strip()
                
                # Mass excess (keV)
                mass_excess_str = line[29:43].strip()
                if '#' in mass_excess_str or '*' in mass_excess_str:
                    continue  # Skip estimated/non-calculable values
                mass_excess = float(mass_excess_str)
                
                # Binding energy per nucleon (keV)
                binding_per_A_str = line[54:67].strip()
                if '#' in binding_per_A_str or '*' in binding_per_A_str:
                    continue
                binding_per_A = float(binding_per_A_str)
                
                # Total binding energy (keV)
                binding_total = binding_per_A * A
                
                nuclides.append({
                    'N': N,
                    'Z': Z,
                    'A': A,
                    'element': el,
                    'mass_excess': mass_excess,  # keV
                    'binding_per_A': binding_per_A,  # keV
                    'binding_total': binding_total,  # keV
                })
                
            except (ValueError, IndexError):
                continue
    
    return nuclides

def compute_separation_energies(nuclides):
    """
    Compute neutron/proton separation energies
    
    S_n(Z,N) = BE(Z,N) - BE(Z,N-1)  (neutron separation energy)
    S_p(Z,N) = BE(Z,N) - BE(Z-1,N)  (proton separation energy)
    """
    # Create lookup by (Z, N)
    be_lookup = {}
    for nuc in nuclides:
        be_lookup[(nuc['Z'], nuc['N'])] = nuc['binding_total']
    
    # Compute separation energies
    for nuc in nuclides:
        Z, N = nuc['Z'], nuc['N']
        
        # Neutron separation energy
        if (Z, N-1) in be_lookup:
            nuc['S_n'] = be_lookup[(Z, N)] - be_lookup[(Z, N-1)]
        else:
            nuc['S_n'] = None
            
        # Proton separation energy
        if (Z-1, N) in be_lookup:
            nuc['S_p'] = be_lookup[(Z, N)] - be_lookup[(Z-1, N)]
        else:
            nuc['S_p'] = None
    
    return nuclides

def find_shell_gaps(nuclides, min_gap_mev=10.0):
    """
    Find significant gaps in separation energies that indicate shell closures
    
    Args:
        nuclides: List of nuclide data
        min_gap_mev: Minimum gap size in MeV to report
    
    Returns:
        List of detected gaps
    """
    gaps = []
    
    # Group by Z (isotopes)
    by_z = defaultdict(list)
    for nuc in nuclides:
        if nuc['S_n'] is not None:
            by_z[nuc['Z']].append(nuc)
    
    # Look for drops in S_n (shell closure)
    for Z in sorted(by_z.keys()):
        isotopes = sorted(by_z[Z], key=lambda x: x['N'])
        
        for i in range(len(isotopes) - 1):
            curr = isotopes[i]
            next_iso = isotopes[i+1]
            
            # Gap = drop in separation energy
            gap = curr['S_n'] - next_iso['S_n']
            gap_mev = gap / 1000.0  # Convert keV to MeV
            
            if gap_mev >= min_gap_mev:
                gaps.append({
                    'Z': Z,
                    'element': curr['element'],
                    'N_before': curr['N'],
                    'N_after': next_iso['N'],
                    'S_n_before': curr['S_n'] / 1000.0,  # MeV
                    'S_n_after': next_iso['S_n'] / 1000.0,  # MeV
                    'gap_mev': gap_mev,
                })
    
    return gaps

def main():
    print("=" * 70)
    print("AME 2020 Nuclear Data Analysis")
    print("=" * 70)
    
    # Parse data
    print("\nParsing AME 2020 data...")
    nuclides = parse_ame2020('ame2020_mass.txt')
    print(f"Loaded {len(nuclides)} nuclides with experimental data")
    
    # Compute separation energies
    print("\nComputing separation energies...")
    nuclides = compute_separation_energies(nuclides)
    
    # Find shell gaps
    print("\nSearching for shell gaps (≥10 MeV)...")
    gaps = find_shell_gaps(nuclides, min_gap_mev=10.0)
    
    print(f"\nFound {len(gaps)} significant gaps (≥10 MeV)")
    print("\nTop 20 largest gaps:")
    print("-" * 70)
    print(f"{'Z':>3} {'El':>3} {'N_before':>8} {'N_after':>8} {'S_n_before':>10} {'S_n_after':>10} {'Gap (MeV)':>10}")
    print("-" * 70)
    
    gaps_sorted = sorted(gaps, key=lambda x: x['gap_mev'], reverse=True)
    for gap in gaps_sorted[:20]:
        print(f"{gap['Z']:>3} {gap['element']:>3} {gap['N_before']:>8} {gap['N_after']:>8} "
              f"{gap['S_n_before']:>10.3f} {gap['S_n_after']:>10.3f} {gap['gap_mev']:>10.3f}")
    
    # Look specifically for gaps near 14 MeV (UFRF prediction)
    print("\n" + "=" * 70)
    print("Gaps near 14.0 ± 0.25 MeV (UFRF prediction range: 13.75-14.25 MeV)")
    print("=" * 70)
    
    ufrf_gaps = [g for g in gaps if 13.75 <= g['gap_mev'] <= 14.25]
    
    if ufrf_gaps:
        print(f"\nFound {len(ufrf_gaps)} gaps in UFRF prediction range:")
        print("-" * 70)
        for gap in sorted(ufrf_gaps, key=lambda x: x['gap_mev'], reverse=True):
            print(f"Z={gap['Z']:>3} ({gap['element']:>3}), N={gap['N_before']:>3}→{gap['N_after']:>3}, "
                  f"S_n: {gap['S_n_before']:.3f}→{gap['S_n_after']:.3f} MeV, Gap={gap['gap_mev']:.3f} MeV")
    else:
        print("\n❌ No gaps found in UFRF prediction range (13.75-14.25 MeV)")
    
    # Statistics
    print("\n" + "=" * 70)
    print("Gap Statistics")
    print("=" * 70)
    gap_values = [g['gap_mev'] for g in gaps]
    print(f"Mean gap: {np.mean(gap_values):.3f} MeV")
    print(f"Median gap: {np.median(gap_values):.3f} MeV")
    print(f"Std dev: {np.std(gap_values):.3f} MeV")
    print(f"Max gap: {np.max(gap_values):.3f} MeV")
    print(f"Min gap: {np.min(gap_values):.3f} MeV (≥10 MeV threshold)")
    
    # Save results
    print("\nSaving results to nuclear_gaps_ame2020.txt...")
    with open('nuclear_gaps_ame2020.txt', 'w') as f:
        f.write("Nuclear Shell Gaps from AME 2020 Data\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Total nuclides analyzed: {len(nuclides)}\n")
        f.write(f"Gaps found (≥10 MeV): {len(gaps)}\n\n")
        f.write("All gaps:\n")
        f.write("-" * 70 + "\n")
        f.write(f"{'Z':>3} {'El':>3} {'N_before':>8} {'N_after':>8} {'S_n_before':>10} {'S_n_after':>10} {'Gap (MeV)':>10}\n")
        f.write("-" * 70 + "\n")
        for gap in gaps_sorted:
            f.write(f"{gap['Z']:>3} {gap['element']:>3} {gap['N_before']:>8} {gap['N_after']:>8} "
                   f"{gap['S_n_before']:>10.3f} {gap['S_n_after']:>10.3f} {gap['gap_mev']:>10.3f}\n")
    
    print("✅ Analysis complete!")

if __name__ == "__main__":
    main()

