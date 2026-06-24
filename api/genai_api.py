import os
from google import genai

client = genai.Client()

# this function sends data to Gemini to return feedback on user actio

def sprout_feedback(action, co2, plant_stage, curr_weather):
	prompt = f"""
	Act as a virtual plant companion set to motivate users to make more 
	enviromentally friendly choices in their day by day. Return feedback on:
	- Action: {action}
	- CO2 reduced: {co2}kg
	- Plant Stage: {plant_stage}
	- Todays Weather: {curr_weather}

	1. Describe how this action helped my plant grow.
	2. Give me a few words of motivation.
	3. Give me a simple eco-challenge for tomorrow based on expected weather.
	4. Keep this at maximum 7 sentences. No bolding or markdown headers.
	"""

	try: 
		return client.models.generate_content(model='gemini-2.5-flash', contents=prompt).text
	except: 
		return "Thanks for helping me grow!"
