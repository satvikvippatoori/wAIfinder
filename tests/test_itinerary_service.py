from unittest.mock import patch

import pytest

from src.itinerary_service import generate_itineraries


MOCK_AI_RESPONSE = """
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


@patch("src.itinerary_service.call_ai")
def test_generate_itineraries_success(mock_call_ai):
    mock_call_ai.return_value = MOCK_AI_RESPONSE

    result = generate_itineraries(
        trip_length=10,
        region="Southeast Asia",
        budget="500-1500",
        styles=["nightlife", "beaches", "food"],
        pace="balanced",
    )

    assert "itineraries" in result
    assert len(result["itineraries"]) == 3
    assert result["comparison"]["recommended_choice"] == "Thailand Escape"


def test_generate_itineraries_invalid_input():
    with pytest.raises(ValueError):
        generate_itineraries(
            trip_length=10,
            region="Southeast Asia",
            budget="500-1500",
            styles=["nightlife", "beaches"],
            pace="balanced",
        )