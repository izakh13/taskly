import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def improve_task_description(description: str) -> str:
    client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
    response = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=f'Rewrite this description and make it clearer in one sentance: {description}.'
    )
    return response.text