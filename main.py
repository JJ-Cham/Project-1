from api.weather_api import suggest_action
from database.db import get_plant, get_actions, create_user, get_user, create_plant, init_db
from game.actions import perform_action
from api.genai_api import sprout_feedback
from sprout.game.plant_art import PLANT_ART

def main():

    init_db()

    username = input("Username: ")

    create_user(username)

    user = get_user(username)

    #create_plant(user["id"], plant_name)

    plant = get_plant(user.id)

    if plant is None:
        plant_name = input("Plant name: ")
        create_plant(user.id, plant_name)

        # reload plant after creation
        plant = get_plant(user.id)

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

            plant = get_plant(user.id)

            if plant is None:
                print("🌱 Creating your first plant...")
                plant_name = input("Plant name: ")
                create_plant(user.id, plant_name)

                plant = get_plant(user.id)

            display_plant(plant)
            print(PLANT_ART[plant.stage])


        elif choice == "2":

            km = float(input("Distance (km): "))
            city = input("City: ")

            feedback = perform_action(
                user.id,
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
                user.id,
                "walk",
                km,
                city
            )

            print("\n🌱 Plant Message:")
            print(feedback)

        elif choice == "4":

            city = input("City: ")

            items = int(input("How many items did you recycle? "))

            feedback = perform_action(
                user.id,
                "recycle",
                items,
                city
            )

            print("\n🌱 Plant Message:")
            print(feedback)

        elif choice == "5":

            km = float(input("Distance (km): "))

            feedback = perform_action(
                user.id,
                "bus",
                km
            )

            print("\n🌱 Plant Message:")
            print(feedback)

        elif choice == "6":
            city = input("City: ")
            print(suggest_action(city))

        elif choice == "7":
            history = get_actions(user.id)

            for action in history:
                print(
                    f"{action.action_type} | "
                    f"{action.carbon_saved} kg CO₂ saved"
                )

        elif choice == "8":
            print("Goodbye 🌱")
            break

def display_plant(plant):

    print("\n===== YOUR PLANT =====")
    if plant is None:
        print("⚠️ No plant found. Please restart or create one.")
    else:
        print("Name:", plant.plant_name)
        print("XP:", plant.xp)
        print("Level:", plant.level)
        print("Stage:", plant.stage)


print("\n🌱 Welcome to Sprout!:")
#print(sprout_feedback)

if __name__ == "__main__":

    main()