import streamlit as st

st.set_page_config(page_title="AI Travel Assistant")

st.title("✈️ AI Travel Assistant")

trip_length = st.number_input(
    "Trip Length (Days)",
    min_value=1,
    max_value=30,
    value=10
)

region = st.text_input(
    "Region or Country"
)

budget = st.selectbox(
    "Budget",
    ["<500", "500-1500", ">1500"]
)

styles = st.multiselect(
    "Pick 3 Styles",
    [
        "nightlife",
        "beaches",
        "food",
        "culture",
        "nature",
        "adventure",
        "shopping",
        "luxury",
        "relaxation"
    ],
    max_selections=3
)

pace = st.selectbox(
    "Travel Pace",
    ["relaxed", "balanced", "fast-paced"]
)

if st.button("Generate Trips"):
    st.write("Generating itineraries...")