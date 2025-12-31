import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
### print("OPENAI_API_KEY loaded:", bool(os.getenv("OPENAI_API_KEY")))
SYSTEM_PROMPT = """
You are an intelligent flight delay assistant.
You do NOT predict delays.
You EXPLAIN and REASON using the provided prediction results.

Rules:
- Base all reasoning strictly on the provided context
- Do not invent new probabilities
- Keep explanations clear and traveler-friendly
- If risk is Low → reassure
- If risk is Medium → caution
- If risk is High → recommend alternatives
"""

def generate_agent_response(user_query: str, context: dict):
    delay_risk = context.get("delay_risk")
    delay_probability = context.get("delay_probability")

    if delay_risk is None or delay_probability is None:
        return "Please predict delay risk first so I can assist you."

    user_prompt = f"""
User question:
{user_query}

Flight delay prediction:
- Delay risk: {delay_risk}
- Delay probability: {delay_probability:.2%}

Explain and advise the user based ONLY on this information.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast + cheap + strong reasoning
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()

