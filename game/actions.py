from api.carbon_api import carbon_saved
from api.weather_api import get_weather
from api.genai_api import sprout_feedback

from database.db import get_plant, log_action
from game.plant_growth import update_plant_progression


def perform_action(user_id, action_type, distance=0, city=""):

    # -----------------------------
    # 1. CALCULATE CARBON SAVED
    # -----------------------------
    if action_type in ["bike", "walk", "bus"]:
        saved = carbon_saved(action_type, distance)

        if saved is None:
            saved = 1.0

    elif action_type == "recycle":
        items_recycled = max(1, int(distance))  # now "distance" = items
        saved = items_recycled * 0.5

    else:
        saved = 0.5


    # -----------------------------
    # 2. LOG ACTION
    # -----------------------------
    log_action(user_id, action_type, saved)


    # -----------------------------
    # 3. XP CALCULATION
    # -----------------------------
    xp_gain = max(1, round(saved * 10))


    # -----------------------------
    # 4. WEATHER (OPTIONAL FLAVOR)
    # -----------------------------
    weather = get_weather(city)
    weather_desc = "Unknown"

    if weather:
        weather_desc = weather["description"]


    # -----------------------------
    # 5. UPDATE PLANT
    # -----------------------------
    update_plant_progression(
        user_id,
        xp_gain,
        0
    )

    plant = get_plant(user_id)

    if plant is None:
        return "No plant found for this user."



    # -----------------------------
    # 6. AI FEEDBACK
    # -----------------------------
    feedback = sprout_feedback(
        action_type,
        saved,
        plant.stage,
        weather_desc
    )


    # -----------------------------
    # 7. RETURN RESULT
    # -----------------------------
    return (
        f"+{xp_gain} XP\n"
        f"{feedback}"
    )