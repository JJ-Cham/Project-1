from api.weather_api import suggest_action
from database.db import init_db, create_user, get_user, create_plant, get_plant, log_action, get_actions


# def main():
#     init_db()

#     create_user("jake")
#     user = get_user("jake")

#     create_plant(user["id"], "Sunflower")
#     plant = get_plant(user["id"])

#     print("PLANT:")
#     print(plant)

#     log_action(user["id"], "bike", 1.8)

#     actions = get_actions(user["id"])

#     print("\nACTIONS:")
#     print(actions)
from database.db import *
from game.actions import perform_action

def main():

    init_db()

    username = input("Username: ")

    create_user(username)

    user = get_user(username)

    plant = get_plant(user["id"])

    if plant is None:

        plant_name = input("Plant name: ")

        create_plant(
            user["id"],
            plant_name
        )

    while True:

        print("\n===== SPROUT =====")
        print("1. View Plant")
        print("2. Bike")
        print("3. Walk")
        print("4. Recycle")
        print("5. Bus")
        print("6. Weather Suggestion")
        print("7. View History")
        print("8. Exit")

        choice = input("> ")

        if choice == "1":

            plant = get_plant(user["id"])

            print(plant)

        elif choice == "2":

            km = float(input("Distance (km): "))
            city = input("City: ")

            feedback = perform_action(
                user["id"],
                "bike",
                km,
                city
            )

            print("\n🌱 Plant Message:")
            print(feedback)

        elif choice == "3":

            km = float(input("Distance (km): "))
            city = input("City: ")

            feedback = perform_action(
                user["id"],
                "walk",
                km,
                city
            )

            print("\n🌱 Plant Message:")
            print(feedback)

        elif choice == "4":

            city = input("City: ")

            feedback = perform_action(
                user["id"],
                "recycle",
                0,
                city
            )

            print("\n🌱 Plant Message:")
            print(feedback)

        elif choice == "5":

            km = float(input("Distance (km): "))

            perform_action(
                user["id"],
                "bus",
                km
            )

        elif choice == "6":
            city = input("City: ")
            print(suggest_action(city))

        elif choice == "7":
            history = get_actions(user["id"])
            print(history)

        elif choice == "8":
            print("Goodbye 🌱")
            break

def display_plant(plant):

    print("\n===== YOUR PLANT =====")

    print("Name:", plant["plant_name"])
    print("XP:", plant["xp"])
    print("Level:", plant["level"])
    print("Stage:", plant["stage"])


print("\n🌱 Plant Message:")
print(sprout_feedback)

if __name__ == "__main__":
    main()