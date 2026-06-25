# import os

# # allow gemini to run
# from google import genai
# from google.genai import errors
import os
from dotenv import load_dotenv

from google import genai
from google.genai import errors

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

load_dotenv(ENV_PATH)

API_KEY = os.getenv("GEMINI_API_KEY")
# ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

# if os.path.exists(ENV_PATH):
#     # safely extract the raw key string, discarding 'export', spaces, and quotes
#     raw_content = open(ENV_PATH).read().split("=")[-1]
#     os.environ["GEMINI_API_KEY"] = raw_content.replace("export", "").strip(' \n\r"\'')

# API_KEY = os.environ.get("GEMINI_API_KEY")

# this function sends data to Gemini to return feedback on user action
def sprout_feedback(action, co2, plant_stage, curr_weather):
    if not API_KEY:
        print("Missing GEMINI_API_KEY. Set it as an environment variable.")
        return None

    client = genai.Client(api_key=API_KEY)

    # incorporate the weather data
    weather_summary = "Unknown"
    if curr_weather and isinstance(curr_weather, dict):
        weather_summary = (
            f"{curr_weather.get('temp')}°C, {curr_weather.get('description')} "
            f"in {curr_weather.get('city')}"
        )

    prompt = f"""
    Act as a virtual plant companion set to motivate users to make more 
    enviromentally friendly choices in their day by day. Return feedback on:
    - Action: {action}
    - CO2 reduced: {co2}kg
    - Plant Stage: {plant_stage}
    - Todays Weather: {weather_summary}

    1. Describe how this action helped my plant grow.
    2. Give me a few words of motivation.
    3. Give me a simple eco-challenge for tomorrow based on expected weather.
    4. Keep this at maximum 7 sentences. Format your output as a clean multi-line paragraph. No bolding or markdown headers.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
    except errors.APIError as error:
        print(f"Gemini request failed: {error}")
        return None

    return response.text

if __name__ == "__main__":
    # file setup for module imports
    pass
