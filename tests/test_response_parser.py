import pytest

from src.response_parser import parse_itinerary_response


VALID_RESPONSE = """
{
  "itineraries": [
    {
      "title": "Thailand Escape",
      "route": ["Bangkok", "Phuket"],
      "best_for": "Nightlife, beaches, and food",
      "pace_fit": "Balanced",
      "summary": "A balanced route through Thailand.",
      "tradeoffs": ["Less cultural variety"],
      "daily_plan": ["Day 1: Arrive in Bangkok"]
    },
    {
      "title": "Singapore and Bali",
      "route": ["Singapore", "Bali"],
      "best_for": "City energy and relaxation",
      "pace_fit": "Balanced",
      "summary": "A city and island combination.",
      "tradeoffs": ["Higher cost"],
      "daily_plan": ["Day 1: Arrive in Singapore"]
    },
    {
      "title": "Taiwan and Hong Kong",
      "route": ["Taipei", "Hong Kong"],
      "best_for": "Food and culture",
      "pace_fit": "Fast-paced",
      "summary": "A food-focused city trip.",
      "tradeoffs": ["Less beach time"],
      "daily_plan": ["Day 1: Arrive in Taipei"]
    }
  ],
  "comparison": {
    "recommended_choice": "Thailand Escape",
    "why": "It best matches nightlife, beaches, and food.",
    "comparison_rows": []
  }
}
"""


def test_parse_valid_response():
    parsed = parse_itinerary_response(VALID_RESPONSE)

    assert "itineraries" in parsed
    assert len(parsed["itineraries"]) == 3
    assert parsed["itineraries"][0]["title"] == "Thailand Escape"
    assert parsed["comparison"]["recommended_choice"] == "Thailand Escape"


def test_parse_response_with_json_code_fence():
    response = f"```json\n{VALID_RESPONSE}\n```"

    parsed = parse_itinerary_response(response)

    assert len(parsed["itineraries"]) == 3


def test_invalid_json_raises_value_error():
    with pytest.raises(ValueError):
        parse_itinerary_response("this is not json")


def test_missing_itineraries_raises_value_error():
    with pytest.raises(ValueError):
        parse_itinerary_response('{"comparison": {}}')


def test_wrong_number_of_itineraries_raises_value_error():
    response = """
    {
      "itineraries": [
        {"title": "Only One Trip"}
      ]
    }
    """

    with pytest.raises(ValueError):
        parse_itinerary_response(response)