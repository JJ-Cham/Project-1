import os
import pandas as pd

# pathing to run from the main project root folder
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db import init_db, create_user, create_plant, get_user, get_plant, log_action
from game.plant_growth import update_plant_progression

# setup files
init_db()

username = "TestUser01"
plant_name = "Sproutly"

# get user
user = get_user(username)
if user is None:
    create_user(username)
    user = get_user(username)

user_id = int(user["id"])

# get plant
plant = get_plant(user_id)
if plant is None:
    create_plant(user_id, plant_name)
    plant = get_plant(user_id)

# save action
log_action(user_id, action_type="Recycling", carbon_saved=5)

# calculate growth and show art
update_plant_progression(user_id, weather_bonus=7, carbon_penalty=0)