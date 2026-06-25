from game.plant_art import PLANT_ART

from database.db import SessionLocal
from database.schema import Plant


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

    db = SessionLocal()

    plant = (
        db.query(Plant)
        .filter(Plant.user_id == user_id)
        .first()
    )

    if plant is None:
        db.close()
        return None

    current_xp = plant.xp
    old_stage = plant.stage

    growth_delta = weather_bonus - carbon_penalty

    new_xp = current_xp + growth_delta

    if new_xp < 0:
        new_xp = 0

    new_stage = get_stage(new_xp)

    plant.xp = new_xp
    plant.stage = new_stage

    db.commit()

    print("\n--- NEW GROWTH ---")
    print("XP:", current_xp, "->", new_xp)
    print("Stage:", new_stage)

    if new_stage in PLANT_ART:
        print(PLANT_ART[new_stage])

    if new_stage != old_stage:
        print("🌱 Your plant evolved into:", new_stage)

    db.close()

    return plant