import pandas as pd
import pytest
import os
from unittest.mock import patch

import database.db as db

# Helper: create empty temp files
@pytest.fixture
def temp_db(tmp_path):
    users = tmp_path / "users.csv"
    plants = tmp_path / "plants.csv"
    actions = tmp_path / "actions.csv"

    # patch file paths inside module
    with patch.object(db, "USERS_FILE", str(users)), \
         patch.object(db, "PLANTS_FILE", str(plants)), \
         patch.object(db, "ACTIONS_FILE", str(actions)):

        yield



# Test init_db creates files
def test_init_db_creates_files(temp_db):
    db.init_db()

    assert os.path.exists(db.USERS_FILE)
    assert os.path.exists(db.PLANTS_FILE)
    assert os.path.exists(db.ACTIONS_FILE)


# Test create_user
def test_create_user(temp_db):
    db.init_db()

    db.create_user("jake")

    df = pd.read_csv(db.USERS_FILE)

    assert len(df) == 1
    assert df.iloc[0]["username"] == "jake"

# Test duplicate user is ignored
def test_create_duplicate_user(temp_db):
    db.init_db()

    db.create_user("jake")
    db.create_user("jake")  # duplicate

    df = pd.read_csv(db.USERS_FILE)

    assert len(df) == 1


# Test get_user
def test_get_user(temp_db):
    db.init_db()

    db.create_user("mike")

    user = db.get_user("mike")

    assert user is not None
    assert user["username"] == "mike"


def test_get_user_not_found(temp_db):
    db.init_db()

    user = db.get_user("ghost")

    assert user is None


# Test create_plant
def test_create_plant(temp_db):
    db.init_db()

    db.create_plant(1, "Sunflower")

    df = pd.read_csv(db.PLANTS_FILE)

    assert len(df) == 1
    assert df.iloc[0]["plant_name"] == "Sunflower"
    assert df.iloc[0]["xp"] == 0
    assert df.iloc[0]["level"] == 1
    assert df.iloc[0]["stage"] == "Seed"

# Test get_plant
def test_get_plant(temp_db):
    db.init_db()

    db.create_plant(5, "Rose")

    plant = db.get_plant(5)

    assert plant is not None
    assert plant["plant_name"] == "Rose"


def test_get_plant_not_found(temp_db):
    db.init_db()

    plant = db.get_plant(999)

    assert plant is None


# Test log_action
def test_log_action(temp_db):
    db.init_db()

    db.log_action(1, "bike", 10.5)

    df = pd.read_csv(db.ACTIONS_FILE)

    assert len(df) == 1
    assert df.iloc[0]["action_type"] == "bike"
    assert df.iloc[0]["carbon_saved"] == 10.5

# Test get_actions
def test_get_actions(temp_db):
    db.init_db()

    db.log_action(1, "walk", 3)
    db.log_action(2, "bike", 5)

    actions = db.get_actions(1)

    assert len(actions) == 1
    assert actions.iloc[0]["action_type"] == "walk"