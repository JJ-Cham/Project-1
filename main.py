from database.schema import create_tables
from database.db import (
    create_user,
    get_user,
    create_plant,
    get_plant,
    log_action,
    get_actions
)


def main():

    create_tables()

    try:
        create_user("jake")
    except Exception:
        pass

    user = get_user("jake")

    create_plant(user["id"], "Sunflower")

    plant = get_plant(user["id"])

    print("Plant:")
    print(dict(plant))

    log_action(
        user["id"],
        "bike",
        1.8
    )

    actions = get_actions(user["id"])

    print("\nActions:")

    for action in actions:
        print(dict(action))


if __name__ == "__main__":
    main()