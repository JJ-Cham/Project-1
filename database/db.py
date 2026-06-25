import pandas as pd
import os

USERS_FILE = "database/users.csv"
PLANTS_FILE = "database/plants.csv"
ACTIONS_FILE = "database/actions.csv"


def init_db():

    if not os.path.exists(USERS_FILE):
        pd.DataFrame(columns=["id", "username"]).to_csv(USERS_FILE, index=False)

    if not os.path.exists(PLANTS_FILE):
        pd.DataFrame(columns=[
            "id", "user_id", "plant_name", "xp", "level", "stage"
        ]).to_csv(PLANTS_FILE, index=False)

    if not os.path.exists(ACTIONS_FILE):
        pd.DataFrame(columns=[
            "id", "user_id", "action_type", "carbon_saved"
        ]).to_csv(ACTIONS_FILE, index=False)

def create_user(username):
    df = pd.read_csv(USERS_FILE)

    if username in df["username"].values:
        return

    #new_id = len(df) + 1
    new_id = df["id"].max() + 1 if not df.empty else 1

    new_row = pd.DataFrame([{
        "id": new_id,
        "username": username
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(USERS_FILE, index=False)


# def get_user(username):
#     df = pd.read_csv(USERS_FILE)
#     user = df[df["username"] == username]

#     if user.empty:
#         return None

#     return user.iloc[0]
def get_user(username):
    df = pd.read_csv(USERS_FILE)
    user = df[df["username"] == username]

    if user.empty:
        return None

    row = user.iloc[0]

    return {
        "id": int(row["id"]),
        "username": row["username"]
    }

def create_plant(user_id, plant_name):
    df = pd.read_csv(PLANTS_FILE)

    new_id = len(df) + 1

    new_row = pd.DataFrame([{
        "id": new_id,
        "user_id": user_id,
        "plant_name": plant_name,
        "xp": 0,
        "level": 1,
        "stage": "Seed"
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(PLANTS_FILE, index=False)


def get_plant(user_id):
    df = pd.read_csv(PLANTS_FILE)

    df["user_id"] = df["user_id"].astype(int)

    plant = df[df["user_id"] == int(user_id)]

    if plant.empty:
        return None

    return plant.iloc[0]

def log_action(user_id, action_type, carbon_saved):
    df = pd.read_csv(ACTIONS_FILE)

    new_id = len(df) + 1

    new_row = pd.DataFrame([{
        "id": new_id,
        "user_id": user_id,
        "action_type": action_type,
        "carbon_saved": carbon_saved
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(ACTIONS_FILE, index=False)


# def get_actions(user_id):
#     df = pd.read_csv(ACTIONS_FILE)
#     return df[df["user_id"] == user_id]
def get_actions(user_id):
    df = pd.read_csv(ACTIONS_FILE)

    df["user_id"] = df["user_id"].astype(int)

    return df[df["user_id"] == int(user_id)]