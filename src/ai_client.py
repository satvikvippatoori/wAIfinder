import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_ai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": (
                    "You are an expert AI travel planner. "
                    "Return valid JSON only.\n\n"
                    + prompt
                ),
            }
        ],
        temperature=0.6,
        reasoning_effort="low",
        reasoning_format="hidden",
        max_completion_tokens=6000,
        response_format={"type": "json_object"},
    )

    return response.choices[0].message.content