from src.prompt_builder import build_itinerary_prompt


def test_prompt_contains_user_inputs():
    prompt = build_itinerary_prompt(
        trip_length=10,
        region="Southeast Asia",
        budget="500-1500",
        styles=["nightlife", "beaches", "food"],
        pace="balanced",
    )

    assert "10 days" in prompt
    assert "Southeast Asia" in prompt
    assert "500-1500" in prompt
    assert "nightlife, beaches, food" in prompt
    assert "balanced" in prompt


def test_prompt_requests_json():
    prompt = build_itinerary_prompt(
        trip_length=7,
        region="Europe",
        budget=">1500",
        styles=["culture", "food", "history"],
        pace="relaxed",
    )

    assert "Return ONLY valid JSON" in prompt
    assert "itineraries" in prompt
    assert "comparison" in prompt