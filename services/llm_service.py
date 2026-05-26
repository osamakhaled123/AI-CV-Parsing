import requests
import json
from helpers.config import get_settings

settings = get_settings()


def call_llm(prompt: str):

    response = requests.post(
        f"{settings.OPENROUTER_BASE_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {settings.API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": settings.OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    response.raise_for_status()

    content = response.json()['choices'][0]['message']['content']
    
    # Remove markdown json fences
    content = content.replace("```json", "").replace("```", "").strip()
    
    return content

    # # Convert string -> Python dict
    # parsed_json = json.loads(content)

    # # Extract only scores
    # scores = parsed_json["matching_scores"]

    # return scores