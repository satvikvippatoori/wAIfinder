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

Important rules:
- The 3 options should be different trip concepts, not tiny variations of the same trip.
- If the user gives a broad region, suggest different routes within or near that region.
- If the user gives a specific country, keep the trips mostly within that country.
- Make the itineraries realistic for the trip length and pace.
- Do not overload relaxed trips.
- Fast-paced trips can include more destinations.
- Budget should influence the destination choices and activity style.
- Include tradeoffs for each itinerary.
- Explain why each itinerary fits the user’s preferences.

For each itinerary, include:
1. Title
2. Route
3. Day split
4. Best for
5. Summary
6. Tradeoffs
7. Day-by-day plan

Return the response in clean markdown with clear headings.
"""