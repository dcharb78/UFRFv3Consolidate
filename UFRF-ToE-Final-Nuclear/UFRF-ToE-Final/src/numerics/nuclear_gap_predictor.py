from __future__ import annotations

def predicted_gap_MeV(index: int) -> float:
    """
    Simple continuation of 2.5, 5.5, 8.5, 11.5 -> 14.5 (intrinsic), then project to 14.0 (observed).
    Index 1..5 returns 2.5, 5.5, 8.5, 11.5, 14.0
    """
    intrinsic = [2.5, 5.5, 8.5, 11.5, 14.5]
    if index < 1 or index > 5:
        raise ValueError("index must be in 1..5")
    val = intrinsic[index-1]
    if index == 5:
        val = 14.0  # projected
    return val
