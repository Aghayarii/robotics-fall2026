import math


def front_distance(
    ranges: Sequence[float],
    angle_min: float,
    angle_increment: float,
    half_width_radians: float,
) -> float | None:
    """Return the nearest finite, positive reading in the front sector.

    Return ``None`` when the sector has no valid reading. Angles are measured in
    radians and the front direction is zero radians.
    """
    valid_distances = []

    for i, distance in enumerate(ranges):
        angle = angle_min + i * angle_increment

        if abs(angle) <= half_width_radians:
            if math.isfinite(distance) and distance > 0:
                valid_distances.append(distance)

    if not valid_distances:
        return None

    return min(valid_distances)


def decide_velocity(
    distance: float | None,
    stop_distance: float,
    forward_speed: float,
) -> float:
    """Return a bounded forward velocity; missing data must produce a stop."""

    if distance is None:
        return 0.0

    if distance <= stop_distance:
        return 0.0

    return max(0.0, forward_speed)
