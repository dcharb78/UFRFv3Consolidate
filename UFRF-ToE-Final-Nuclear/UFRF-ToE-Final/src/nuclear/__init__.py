"""
UFRF Nuclear Shell Model

Derives nuclear shell magic numbers from first principles using:
- Cuboctahedron musical geometry
- M=144 Hz base frequency (nuclear scale)
- Trinity structure (E×B×B')
- 13-cycle phase space
- Musical chord harmonic structures

Author: Daniel Charboneau
"""

from .shell_model import (
    generate_shell_structure,
    validate_against_known,
    degeneracy_at_level,
    cumulative_nucleons,
    chord_structure,
    trinity_interference,
    frequency_at_position,
)

__all__ = [
    'generate_shell_structure',
    'validate_against_known',
    'degeneracy_at_level',
    'cumulative_nucleons',
    'chord_structure',
    'trinity_interference',
    'frequency_at_position',
]

__version__ = '1.0.0'
__author__ = 'Daniel Charboneau'

