from os import system

UNSET_OPTION = -1
EXIT_OPTION = 6

def display_get_choice():
    print("=== WELCOME TO JAKIM LOPEZ'S PROFILE ===")
    print("1. Get to know me better")
    print("2. Goals in life")
    print("3. Miko's comment")
    print("4. Kyle's comment")
    print("5. Hanz's comment")
    print("6. Pearl's Comment")
    
    try:
        choice = int(input("Enter your choice:"))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("Invalid input.")
        return UNSET_OPTION