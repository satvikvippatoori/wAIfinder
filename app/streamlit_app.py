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


st.markdown(
    """
    <style>

        .stApp {
            background: #f8fafc;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        /* SIDEBAR */

        [data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #ede9fe 0%,
                #f8fafc 100%
            );
            border-right: 1px solid #ddd6fe;
        }

        [data-testid="stSidebar"] * {
            color: #1e293b;
        }

        /* HERO */

        .hero-title {
            font-size: 2.5rem;
            font-weight: 850;
            color: #0f172a;
            margin-bottom: 0.2rem;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            color: #64748b;
            margin-bottom: 1.8rem;
        }

        /* BRAND */

        .brand-box {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 1.5rem;
        }

        .brand-icon {
            width: 54px;
            height: 54px;
            border-radius: 18px;
            background: linear-gradient(
                135deg,
                #8b5cf6,
                #6366f1
            );
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            color: white;
            box-shadow: 0 10px 20px rgba(99,102,241,0.25);
        }

        .brand-title {
            font-size: 1.5rem;
            font-weight: 850;
            color: #111827;
        }

        .brand-subtitle {
            font-size: 0.92rem;
            color: #64748b;
        }

        /* SECTION LABELS */

        .section-label {
            font-size: 0.78rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.09em;
            font-weight: 800;
            margin-top: 1rem;
            margin-bottom: 0.4rem;
        }

        /* CARDS */

        [data-testid="stVerticalBlock"] > div:has(.card-header) {
            background: linear-gradient(
                180deg,
                #ffffff 0%,
                #faf5ff 100%
            );

            border: 1px solid #e9d5ff;
            border-radius: 24px;

            padding: 1.6rem;

            box-shadow:
                0 10px 30px rgba(15,23,42,0.06);

            margin-bottom: 1.4rem;
        }

        /* OPTION BADGE */

        .option-badge {
            padding: 0.55rem 0.85rem;
            border-radius: 14px;

            background: linear-gradient(
                135deg,
                #8b5cf6,
                #6366f1
            );

            color: white;
            font-weight: 800;
            font-size: 0.9rem;
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.2rem;
        }

        /* ROUTE PILLS */

        .route-pill {
            display: inline-block;

            background: #ede9fe;
            color: #4c1d95;

            padding: 0.45rem 0.8rem;
            border-radius: 999px;

            font-size: 0.88rem;
            font-weight: 600;

            margin-right: 0.35rem;
            margin-bottom: 0.35rem;
        }

        .arrow {
            color: #8b5cf6;
            font-weight: 700;
            margin-right: 0.35rem;
        }

        /* RECOMMENDED BOX */

        .recommend-box {
            padding: 1.5rem;

            border-radius: 24px;

            background: linear-gradient(
                135deg,
                #8b5cf6 0%,
                #6366f1 100%
            );

            color: white;

            box-shadow:
                0 14px 40px rgba(99,102,241,0.25);

            margin-bottom: 1.8rem;
        }

        .recommend-box .section-label {
            color: rgba(255,255,255,0.75);
        }

        /* HELPER BOX */

        .helper-box {
            padding: 1rem;
            border-radius: 18px;

            background: rgba(255,255,255,0.65);

            border: 1px solid rgba(255,255,255,0.6);

            color: #4c1d95;
            font-size: 0.92rem;

            margin-top: 1rem;
        }

        /* BUTTON */

        .stButton button {
            background: linear-gradient(
                135deg,
                #8b5cf6,
                #6366f1
            ) !important;

            color: white !important;

            border: none !important;

            border-radius: 14px !important;

            font-weight: 700 !important;

            height: 3rem !important;

            box-shadow:
                0 10px 24px rgba(99,102,241,0.2);
        }

        .stButton button:hover {
            filter: brightness(1.05);
        }

    </style>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.markdown(
        """
        <div class="brand-box">
            <div class="brand-icon">✈️</div>
            <div>
                <div class="brand-title">wAIfinder</div>
                <div class="brand-subtitle">Your AI Travel Assistant</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown("### 🧳 Trip Preferences")

    trip_length = st.number_input("Trip Length (days)", min_value=1, max_value=30, value=10)

    region = st.text_input(
        "Region or Country",
        placeholder="Example: Southeast Asia, France",
    )

    budget = st.selectbox("Budget, excluding flights", BUDGET_OPTIONS)

    styles = st.multiselect(
        "Pick exactly 3 travel styles",
        STYLE_OPTIONS,
        max_selections=3,
    )

    pace = st.selectbox("Travel Pace", PACE_OPTIONS)

    st.divider()

    generate_button = st.button("✨ Generate Trips", type="primary", width="stretch")

    st.markdown(
        """
        <div class="helper-box">
            💡 The AI will generate 3 distinct trip options based on your preferences and help you compare them.
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown('<div class="hero-title">Your Trip Options</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Explore 3 unique trip ideas crafted around your budget, pace, and travel style.</div>',
    unsafe_allow_html=True,
)


def render_route(route: list[str]):
    html = ""
    for i, place in enumerate(route):
        html += f'<span class="route-pill">📍 {place}</span>'
        if i < len(route) - 1:
            html += '<span class="arrow">→</span>'
    st.markdown(html, unsafe_allow_html=True)


def render_itinerary_card(itinerary: dict, index: int):
    with st.container(border=True):
        st.markdown(
            f"""
            <div class="card-header">
                <h3>Option {index}: {itinerary.get("title", "Untitled Trip")}</h3>
                <div class="option-badge">#{index}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="section-label">Route</div>', unsafe_allow_html=True)
        render_route(itinerary.get("route", []))

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="section-label">Best For</div>', unsafe_allow_html=True)
            st.markdown(f"👥 **{itinerary.get('best_for', 'N/A')}**")

        with col2:
            st.markdown('<div class="section-label">Pace Fit</div>', unsafe_allow_html=True)
            st.markdown(f"⏱️ **{itinerary.get('pace_fit', 'N/A')}**")

        st.markdown('<div class="section-label">Summary</div>', unsafe_allow_html=True)
        st.write(itinerary.get("summary", ""))

        st.markdown('<div class="section-label">Tradeoffs</div>', unsafe_allow_html=True)
        for tradeoff in itinerary.get("tradeoffs", []):
            st.write(f"• {tradeoff}")

        with st.expander("View day-by-day plan"):
            for day in itinerary.get("daily_plan", []):
                st.write(day)


def render_comparison(comparison: dict):
    recommended = comparison.get("recommended_choice", "N/A")
    why = comparison.get("why", "")

    st.markdown(
        f"""
        <div class="recommend-box">
            <div class="section-label">Recommended Choice</div>
            <h3>✨ {recommended}</h3>
            <p>{why}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("**1. Add preferences**\n\nChoose your region, budget, styles, and pace.")

    with col2:
        st.info("**2. Generate routes**\n\nThe AI creates 3 distinct trip concepts.")

    with col3:
        st.info("**3. Compare tradeoffs**\n\nPick the trip that best matches your travel style.")


if generate_button:
    try:
        with st.spinner("Crafting your trip options..."):
            result = generate_itineraries(
                trip_length=trip_length,
                region=region,
                budget=budget,
                styles=styles,
                pace=pace,
            )

        render_comparison(result.get("comparison", {}))

        st.subheader("Your Trip Options")

        for index, itinerary in enumerate(result["itineraries"], start=1):
            render_itinerary_card(itinerary, index)

    except ValueError as e:
        st.error(str(e))

    except Exception as e:
        st.error("Something went wrong while generating your trips.")
        st.write(e)
else:
    render_empty_state()