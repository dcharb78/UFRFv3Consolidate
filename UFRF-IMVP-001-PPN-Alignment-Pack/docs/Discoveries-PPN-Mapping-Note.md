
# PPN Mapping Note (Orbital → 13‑cycle)

Replace any toy mapping such as "days mod 13" with the same orbital‑phase mapping
used by your existing `ppn_complete_derivation.py`. Document, in that file’s header
comment, how orbital parameters are converted to cycle position `p`, and define
`Δp = p − 10` for the near‑REST expansion.

**Why this matters.** The repository’s PPN results (|γ−1| ≈ 10⁻⁹) imply `Δp ≈ 10⁻⁴.⁵`,
i.e. Earth is extremely close to REST in that mapping. Encoding this explicitly will
prevent unit‑mixing and stabilize future extensions.
