from src.input_validator import validate_inputs
from src.prompt_builder import build_itinerary_prompt
from src.ai_client import call_ai


def generate_itineraries(
    trip_length: int,
    region: str,
    budget: str,
    styles: list[str],
    pace: str,
) -> str:
    is_valid, error_message = validate_inputs(
        trip_length=trip_length,
        region=region,
        budget=budget,
        styles=styles,
        pace=pace,
    )

    if not is_valid:
        raise ValueError(error_message)

    prompt = build_itinerary_prompt(
        trip_length=trip_length,
        region=region,
        budget=budget,
        styles=styles,
        pace=pace,
    )

    return call_ai(prompt)