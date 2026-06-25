from api.carbon_api import carbon_saved
from api.weather_api import get_weather
from api.genai_api import sprout_feedback

from database.db import get_plant, log_action
from game.plant_growth import update_plant_progression


def perform_action(user_id, action_type, distance=0, city="Atlanta"):

    if action_type in ["bike", "walk", "bus"]:

        saved = carbon_saved(action_type, distance)

        if saved is None:
            saved = 1.0

    else:
        saved = 0.5

    log_action(
        user_id,
        action_type,
        saved
    )


    update_plant_progression(
        user_id,
        weather_bonus,
        0
    )

    plant = get_plant(user_id)

    if plant is None:
        return "No plant found for this user."

    weather = get_weather(city)

    weather_desc = "Unknown"

    if weather:
        weather_desc = weather["description"]

    feedback = sprout_feedback(
        action_type,
        saved,
        weather_desc,
        plant_stage = plant["stage"] if plant else "Seed"
    )

    return feedback