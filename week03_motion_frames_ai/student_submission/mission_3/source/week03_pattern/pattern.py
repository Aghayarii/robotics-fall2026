"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name == "rounded_rectangle":
        straight_speed = 0.15
        straight_duration = 2.0
        arc_speed = 0.15
        angular_speed = 0.15
        arc_duration = (math.pi /2) / angular_speed
        segments=[]
        for _ in range(4):
            segments.append(
                Segment(straight_speed, 0.0, straight_duration)
            )
            segments.append(
                Segment(arc_speed, angular_speed, arc_duration)
            )
        return segments
    return []
