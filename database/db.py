from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.schema import Base, User, Plant, Action


DATABASE_URL = "sqlite:///sprout/database/sprout.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def init_db():
    Base.metadata.create_all(bind=engine)

# USER FUNCTIONS
def create_user(username):
    db = SessionLocal()

    existing = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if existing:
        db.close()
        return existing

    user = User(username=username)

    db.add(user)
    db.commit()
    db.refresh(user)

    db.close()

    return user


def get_user(username):
    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    db.close()

    return user

# PLANT FUNCTIONS
def create_plant(user_id, plant_name):
    db = SessionLocal()

    plant = Plant(
        user_id=user_id,
        plant_name=plant_name,
        xp=0,
        level=1,
        stage="Seed"
    )

    db.add(plant)
    db.commit()
    db.refresh(plant)

    db.close()

    return plant


def get_plant(user_id):
    db = SessionLocal()

    plant = (
        db.query(Plant)
        .filter(Plant.user_id == user_id)
        .first()
    )

    db.close()

    return plant

# ACTION FUNCTIONS
def log_action(user_id, action_type, carbon_saved):
    db = SessionLocal()

    action = Action(
        user_id=user_id,
        action_type=action_type,
        carbon_saved=carbon_saved
    )

    db.add(action)
    db.commit()

    db.close()


def get_actions(user_id):
    db = SessionLocal()

    actions = (
        db.query(Action)
        .filter(Action.user_id == user_id)
        .all()
    )

    db.close()

    return actions