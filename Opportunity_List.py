
import json
from datetime import datetime

opportunity = []

categories = ["Hackathon","Stemathon","Olympiad","Internship","Other"]

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None

def save_data():
    with open("opportunities.json","w")as file:
        json.dump(opportunity, file, indent=4)

def load_data():
    global opportunity

    try:
        with open("opportunities.json","r")as file:
            opportunity = json.load(file)

    except FileNotFoundError:
        opportunity=[]

def add_category():
    print("\n choose a categoryof the event")
    
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")
    
    choice= input("enter number: ")
    
    if choice.isdigit():
        choice= int(choice)
        
        if 1<= choice <= len(categories):
            selected = categories[choice -1]
            
            if selected == "Other":
                custom = input(" enter custom category")
  
                return custom 
                
    
            return selected
    
    print("invalid choice, defaulting to other")
    return "Other"

def add_opportunity():
    name= input(" enter the name of the event")
    if not name:
        print("name cannot be empty")
        return
    
    category= add_category()

    reg_date_str = input(" enter the last date to register for the event \n (the last date to register for the event) in YYYY-MM-DD\n")
    start_date_str= input("enter the starting date for the event\n (the date on which event will start) in YYYY-MM-DD \n ")
    end_date_str = input("enter the end date of the event \n (the date on which event will be over)in YYYY-MM-DD \n")
    
    reg_date = parse_date(reg_date_str)
    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)

    if not reg_date or not start_date or not end_date:
        print("invalid date or format! Use correct date and format of YYYY-MM-DD ")
        return
    
    if not (reg_date <= start_date <= end_date):
        print("date order is not correct. registrating date should be the closest and starting date closer than end date from today")
        return
    

    event_details = {
        "name": name,
        "category" : category,
        "last date for registration": reg_date_str,
        "starting date of the event": start_date_str,
        "end date of the event": end_date_str,
    }
    
    opportunity.append(event_details)
    save_data()
    print("event added succesfully")

def view_opportunity():
    if not opportunity:
        print("no event added")
        return
    
    print("\n ***** All events *****")
    for i, event in enumerate(opportunity, start=1):
        print(f"""
              {i}. {event['name']}
              category :{event['category']}
              last date for registration:{event['last date for registration']}
              starting date :{event['starting date of the event']}
              ending date: {event['end date of the event']}
""")
        
load_data()

while True:
    print("\n ***** EVENT LIST FOR STEM STUDENTS TO BOOST THERE CARRIER *****")
    print("1. Add Events")
    print("2. View event")
    print("3. Exit")
    
    choice= input("choose an option between 1, 2 and 3-\n")
    if choice == "1":
        add_opportunity()
        
    elif choice == "2":
        view_opportunity()
    
    elif choice == "3":
        print("BYE!")
        break
    
    else:
        print("invalid choice or spelling error")
