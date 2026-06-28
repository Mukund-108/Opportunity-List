import json
from datetime import datetime

opportunity = []

categories = ["Hackathon", "Stemathon", "Olympiad", "Internship", "Other"]


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None


def save_data():
    with open("opportunities.json", "w") as file:
        json.dump(opportunity, file, indent=4)


def load_data():
    global opportunity

    try:
        with open("opportunities.json", "r") as file:
            opportunity = json.load(file)

    except FileNotFoundError:
        opportunity = []


def add_category():
    print("\nChoose a category of the event")

    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")

    choice = input("Enter number: ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(categories):
            selected = categories[choice - 1]

            if selected == "Other":
                custom = input("Enter custom category: ")
                return custom

            return selected

    print("Invalid choice, defaulting to Other")
    return "Other"


def add_opportunity():
    name = input("Enter the name of the event: ")

    if not name:
        print("Name cannot be empty")
        return

    category = add_category()

    reg_date_str = input(
        "Enter the last date to register (YYYY-MM-DD): "
    )
    start_date_str = input(
        "Enter the starting date (YYYY-MM-DD): "
    )
    end_date_str = input(
        "Enter the end date (YYYY-MM-DD): "
    )

    reg_date = parse_date(reg_date_str)
    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)

    if not reg_date or not start_date or not end_date:
        print("Invalid date! Use YYYY-MM-DD format.")
        return

    if not (reg_date <= start_date <= end_date):
        print("Date order is incorrect.")
        return

    event_details = {
        "name": name,
        "category": category,
        "last date for registration": reg_date_str,
        "starting date of the event": start_date_str,
        "end date of the event": end_date_str,
    }

    opportunity.append(event_details)
    save_data()

    print("Event added successfully!")


def view_opportunity():
    if not opportunity:
        print("No events added.")
        return

    print("\n***** ALL EVENTS *****")

    for i, event in enumerate(opportunity, start=1):
        print(f"""
{i}. {event['name']}
Category: {event['category']}
Last Registration Date: {event['last date for registration']}
Starting Date: {event['starting date of the event']}
Ending Date: {event['end date of the event']}
""")


def main():
    load_data()

    while True:
        print("\n***** EVENT LIST FOR STEM STUDENTS TO BOOST THEIR CAREER *****")
        print("1. Add Event")
        print("2. View Events")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_opportunity()

        elif choice == "2":
            view_opportunity()

        elif choice == "3":
            print("Bye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
