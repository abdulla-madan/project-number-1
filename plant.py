import csv
import uuid
from datetime import date, datetime, timedelta

def add_plant():
    try:
        with open('plants.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Watering frequency'] = int(row['Watering frequency'])
                
        print('\nplants.csv exist.')
    except :
        with open('plants.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ 'plant name/species', 'Location in home', 'date acquired', 'Watering frequency', 'Sunlight needs'])
            print('\n\nnew plants.csv created')
    print("\n=== Add a New plant ===")
    plant_name_species = input("Enter plant name: ")
    
    while True:
        print("Please enter the location of the plant in home.")
        location_in_home = input("Enter : ").lower()
        break

    





















 log_plant_care()
























def display_menu():
    """Display the main menu options."""
    print("\n=== plant Tracker ===")
    print("1. Add a new plant to track")
    print("2.Record a plant care activity ")
    print("3.View plants due for care ")
    print("4.Search plants by name or location")
    print("5.View all plants")
    return input("Enter your choice (1-5): ")








def main():
    """Main application function."""
    print("Welcome to  Plant Care Tracker")
    print("This app is for plant enthusiasts to track their houseplants")

    while True:
        choice = display_menu()

        if choice == '1':
            add_plant()
        elif choice == '2':
            log_plant_care()
        elif choice == '3':
            view_plant_due_care()
        elif choice == '4':
            plant_search()
        elif choice == '5':
            view_all_plant()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
