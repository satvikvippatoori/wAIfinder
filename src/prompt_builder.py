def build_itinerary_prompt(
    trip_length: int,
    region: str,
    budget: str,
    styles: list[str],
    pace: str,
) -> str:
    styles_text = ", ".join(styles)

    return f"""
Create 3 meaningfully different travel itinerary options for the user.

User preferences:
- Trip length: {trip_length} days
- Region or country: {region}
- Budget: {budget}, not including flights
- Top travel styles: {styles_text}
- Travel pace: {pace}

Rules:
- Each option must be a different trip concept, not tiny variations of the same trip.
- If the user gives a broad region, suggest different routes within or near that region.
- If the user gives a specific country, keep the trips mostly within that country.
- Make the itineraries realistic for the trip length and pace.
- Include realistic tradeoffs.
- Keep each daily_plan item under 20 words.
- Keep each summary under 60 words.
- Include exactly 2 tradeoffs per itinerary.
- The daily_plan must contain exactly {trip_length} entries.
- The recommendation should choose the best overall fit for the user's preferences.

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations outside JSON.

Use this exact schema:
{{
  "itineraries": [
    {{
      "title": "string",
      "route": ["string"],
      "best_for": "string",
      "pace_fit": "string",
      "summary": "string",
      "tradeoffs": ["string"],
      "daily_plan": ["Day 1: string"]
    }}
  ],
  "comparison": {{
    "recommended_choice": "string",
    "why": "string",
    "comparison_rows": [
      {{
        "trip": "string",
        "best_for": "string",
        "pace_fit": "string",
        "main_tradeoff": "string"
      }}
    ]
  }}
}}
"""