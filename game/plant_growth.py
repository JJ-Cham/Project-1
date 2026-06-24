import pandas as pd
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


def update_plant_progression(user_id, weather_bonus, carbon_penalty):
    df = pd.read_csv(PLANTS_FILE)

    # locate user row
    user_rows = df[df["user_id"] == user_id]

    if user_rows.empty:
        return None

    plant_row = user_rows.iloc[0]

    # get past values - cast directly to an int
    current_xp = int(plant_row["xp"])
    old_stage = str(plant_row["stage"])

    # determining growth with given integer data
    base_growth = 5
    growth_delta = base_growth + int(weather_bonus) - int(carbon_penalty)
    new_xp = current_xp + growth_delta

    # score never is below zero
    if new_xp < 0:
        new_xp = 0

    new_stage = get_stage(new_xp)

    # modifications directly back to DataFrame column selections as integers
    df.loc[df["user_id"] == user_id, "xp"] = int(new_xp)
    df.loc[df["user_id"] == user_id, "stage"] = new_stage
    df.to_csv(PLANTS_FILE, index=False)

    # game output
    print("\n\n")

    print("--- NEW GROWTH ---")
    print("Points:", current_xp, "->", new_xp)
    print("Current Growth Stage:", new_stage)

    if new_stage in PLANT_ART:
        print(PLANT_ART[new_stage])

    if new_stage != old_stage:
        print("Your plant is now at stage: ", new_stage, ":)")

    print("\n\n")
