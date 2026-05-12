import json
import re


def parse_itinerary_response(response_text: str) -> dict:
    """
    Parses AI response into a Python dictionary.
    Handles cases where the model wraps JSON in code fences.
    """

    cleaned = response_text.strip()

    cleaned = re.sub(r"^```json", "", cleaned)
    cleaned = re.sub(r"^```", "", cleaned)
    cleaned = re.sub(r"```$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError(f"AI response was not valid JSON: {e}")

    if "itineraries" not in data:
        raise ValueError("AI response missing 'itineraries' field.")

    if len(data["itineraries"]) != 3:
        raise ValueError("AI response must contain exactly 3 itineraries.")

    if "comparison" not in data:
        data["comparison"] = {
            "recommended_choice": data["itineraries"][0].get("title", "Option 1"),
            "why": "This option appears to best match the selected preferences.",
            "comparison_rows": [],
        }

    return data