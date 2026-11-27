import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def improve_task_description(description: str) -> str:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    promt = "Rewrite this description and make it clearer in one sentance"
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"{promt}: {description}.",
    )
    return response.text
