from src.input_validator import validate_inputs


def test_valid_inputs():
    is_valid, error = validate_inputs(
        trip_length=10,
        region="Southeast Asia",
        budget="500-1500",
        styles=["nightlife", "beaches", "food"],
        pace="balanced",
    )

    assert is_valid is True
    assert error == ""


def test_invalid_trip_length():
    is_valid, error = validate_inputs(
        trip_length=0,
        region="Southeast Asia",
        budget="500-1500",
        styles=["nightlife", "beaches", "food"],
        pace="balanced",
    )

    assert is_valid is False
    assert error == "Trip length must be greater than 0."


def test_missing_region():
    is_valid, error = validate_inputs(
        trip_length=10,
        region="",
        budget="500-1500",
        styles=["nightlife", "beaches", "food"],
        pace="balanced",
    )

    assert is_valid is False
    assert error == "Please enter a region or country."


def test_requires_exactly_three_styles():
    is_valid, error = validate_inputs(
        trip_length=10,
        region="Southeast Asia",
        budget="500-1500",
        styles=["nightlife", "beaches"],
        pace="balanced",
    )

    assert is_valid is False
    assert error == "Please select exactly 3 travel styles."