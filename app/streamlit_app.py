import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.constants import STYLE_OPTIONS, BUDGET_OPTIONS, PACE_OPTIONS
from src.itinerary_service import generate_itineraries


st.set_page_config(
    page_title="wAIfinder",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ wAIfinder: Your AI Travel Planner")
st.write(
    "Generate 3 distinct trip ideas based on your region, budget, travel style, and pace."
)

with st.sidebar:
    st.header("Trip Preferences")

    trip_length = st.number_input(
        "Trip Length (days)",
        min_value=1,
        max_value=30,
        value=10,
    )

    region = st.text_input(
        "Region or Country",
        placeholder="Example: Southeast Asia, France",
    )

    budget = st.selectbox(
        "Budget, excluding flights",
        BUDGET_OPTIONS,
    )

    styles = st.multiselect(
        "Pick exactly 3 travel styles",
        STYLE_OPTIONS,
        max_selections=3,
    )

    pace = st.selectbox(
        "Travel Pace",
        PACE_OPTIONS,
    )

    generate_button = st.button("Generate Trips", type="primary")


if generate_button:
    try:
        with st.spinner("Generating your trip options..."):
            result = generate_itineraries(
                trip_length=trip_length,
                region=region,
                budget=budget,
                styles=styles,
                pace=pace,
            )

        st.subheader("Your Trip Options")
        st.markdown(result)

    except ValueError as e:
        st.error(str(e))

    except Exception as e:
        st.error("Something went wrong while generating your trips.")
        st.write(e)
else:
    st.info("Enter your trip preferences in the sidebar and click Generate Trips.")