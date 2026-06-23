from database.db import init_db, create_user, get_user, create_plant, get_plant, log_action, get_actions


def main():
    init_db()

    create_user("jake")
    user = get_user("jake")

    create_plant(user["id"], "Sunflower")
    plant = get_plant(user["id"])

    print("PLANT:")
    print(plant)

    log_action(user["id"], "bike", 1.8)

    actions = get_actions(user["id"])

    print("\nACTIONS:")
    print(actions)


if __name__ == "__main__":
    main()