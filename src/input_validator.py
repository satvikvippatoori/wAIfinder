def validate_inputs(
    trip_length: int,
    region: str,
    budget: str,
    styles: list[str],
    pace: str,
) -> tuple[bool, str]:
    if trip_length <= 0:
        return False, "Trip length must be greater than 0."

    if not region.strip():
        return False, "Please enter a region or country."

    if not budget:
        return False, "Please select a budget."

    if len(styles) != 3:
        return False, "Please select exactly 3 travel styles."

    if not pace:
        return False, "Please select a travel pace."

    return True, ""