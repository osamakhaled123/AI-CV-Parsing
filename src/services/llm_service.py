import requests
import json
from helpers.config import get_settings

app_settings = get_settings()


def call_llm(prompt: str):

    response = requests.post(
        f"{app_settings.OPENROUTER_BASE_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {app_settings.API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": app_settings.OPENROUTER_MODEL,
            "temperature": 0,
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
    
    #return content

    # Convert string -> Python dict
    parsed_json = json.loads(content)

    # Extract only scores
    
    #scores = parsed_json["Matching scores"]

    return {"filename":parsed_json[-1]["filename"],
            "Matching_scores":parsed_json[-1]["Matching scores"]}