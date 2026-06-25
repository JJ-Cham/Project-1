import pandas as pd
from api.carbon_api import carbon_saved
from game.plant_art import PLANT_ART

PLANTS_FILE = "database/plants.csv"


def get_stage(xp):
    if xp < 10:
        return "Seed"
    elif xp < 20:
        return "Sprout"
    elif xp < 30:
        return "Seedling"
    elif xp < 40:
        return "Young Plant"
    else:
        return "Blooming Plant"


def update_plant_progression(user_id, weather_bonus, carbon_penalty, action_type=None, distance=None):
    df = pd.read_csv(PLANTS_FILE)

    user_rows = df[df["user_id"] == user_id]
    if user_rows.empty:
        return None

    plant_row = user_rows.iloc[0]

    current_xp = int(plant_row["xp"])
    old_stage = str(plant_row["stage"])

    # FIX: properly compute carbon_saved
    if action_type is not None and distance is not None:
        carbon_value = carbon_saved(action_type, distance)
    else:
        carbon_value = 0

    carbon_value = 0  # handle None safely

    growth_delta = int(carbon_value * 10) + int(weather_bonus) - int(carbon_penalty)

    new_xp = max(0, current_xp + growth_delta)

    new_stage = get_stage(new_xp)

    df.loc[df["user_id"] == user_id, "xp"] = int(new_xp)
    df.loc[df["user_id"] == user_id, "stage"] = new_stage
    df.to_csv(PLANTS_FILE, index=False)

    print("\n\n--- NEW GROWTH ---")
    print("Points:", current_xp, "->", new_xp)
    print("Current Growth Stage:", new_stage)

    if new_stage in PLANT_ART:
        print(PLANT_ART[new_stage])

    if new_stage != old_stage:
        print("Your plant is now at stage:", new_stage, ":)")

    print("\n\n")