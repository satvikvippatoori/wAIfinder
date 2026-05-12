# wAIfinder ✈️

An AI-powered travel planning assistant that generates personalized, tradeoff-aware trip recommendations based on a user’s travel preferences, budget, pace, and destination interests.

wAIfinder helps users compare multiple distinct trip concepts rather than generating a single generic itinerary. The application leverages generative AI to create realistic travel routes, explain tradeoffs, and produce day-by-day travel suggestions through an interactive Streamlit interface.

---

## Features

- Generate 3 distinct trip concepts from a single set of preferences
- AI-powered itinerary generation using LLM APIs
- Personalized recommendations based on:
  - Trip length
  - Region/country
  - Budget
  - Travel styles
  - Travel pace
- Tradeoff-aware trip suggestions
- Multi-city route generation
- Day-by-day travel plans
- Modern interactive Streamlit UI

---

## Example Inputs

- **Trip Length:** 10 days
- **Region:** Southeast Asia
- **Budget:** 500–1500
- **Styles:** nightlife, beaches, food
- **Pace:** balanced

---

## Example Outputs

### Option 1 — Thailand Escape
Bangkok → Phuket → Phi Phi

Best for nightlife, beaches, and food.

---

### Option 2 — Singapore + Bali
Singapore → Bali

Best for luxury, relaxation, and modern city experiences.

---

### Option 3 — Taiwan + Hong Kong
Taipei → Hong Kong

Best for food, culture, and urban exploration.

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Integration
- Groq API
- Llama 3.1 8B Instant

### Libraries
- python-dotenv
- groq

---

## Architecture

```text
User Input
   ↓
Input Validation
   ↓
Prompt Builder
   ↓
Groq LLM API
   ↓
JSON Response Parsing
   ↓
Recommendation Rendering
   ↓
Interactive UI
Project Structure
travel-ai-assistant/
│
├── app/
│   ├── streamlit_app.py
│   └── constants.py
│
├── src/
│   ├── ai_client.py
│   ├── input_validator.py
│   ├── itinerary_service.py
│   ├── prompt_builder.py
│   └── response_parser.py
│
├── prompts/
│
├── tests/
│
├── requirements.txt
├── .env
└── README.md

Installation
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/travel-ai-assistant.git
cd travel-ai-assistant
2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Create .env
GROQ_API_KEY=your_api_key_here
5. Run Application
streamlit run app/streamlit_app.py
Key Design Decisions
Structured Inputs Over Free-Form Prompting

The application uses structured user inputs to create more reliable and personalized itinerary generation.

Multiple Trip Concepts Instead of One Itinerary

Instead of generating a single route, the AI creates multiple distinct travel directions to help users compare tradeoffs and choose the best experience for their preferences.

JSON-Based AI Responses

The LLM is prompted to return structured JSON outputs for reliable parsing and rendering in the frontend.

Tradeoff-Aware Recommendations

The AI explains not only what each trip offers, but also the compromises associated with each route.

Future Improvements
Flight integration
Hotel recommendations
Budget estimation engine
Interactive maps
Save/share itineraries
User accounts
Real-time weather integration
Screenshots

Add screenshots here after deployment.

Author
Satvik Vippatoori
