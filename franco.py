import os

BORDER = "=" * 47

def clear_screen():
    os.system("cls")

def print_border():
    print(BORDER)

def return_to_main_menu():
    print("Press Enter to return to the main menu...")
    input()

def display_section(func):
    clear_screen()
    func()

def basic_information():
    print("BASIC INFORMATION:")
    print_border()
    print("Name: Fernette Pearl Franco")
    print("Age: 19")
    print("Gender: Female")
    print("Occupation: Student (Aspiring Web Developer)")
    print("Location: Bagumbayan, Taguig City, Philippines")
    print("School: Polytechnic University of the Philippines")
    print("Course: Bachelor of Science in Information Technology")
    print_border()
    return_to_main_menu()

def goals():
    print("GOALS:")
    print_border()
    print("1. To become a great web developer.")
    print("2. To contribute to major projects that will be impactful.")
    print("3. To learn new programming languages and frameworks.")
    print("4. To build a personal portfolio website (on going).")
    print_border()
    return_to_main_menu()

def skills():
    print("SKILLS:")
    print_border()
    print("1. HTML, CSS, JavaScript")
    print("2. Python (Kinda working on it)")
    print("3. Painting and Singing")
    print("4. Familiar with Git and GitHub")
    print("5. Problem-solving and analytical skills (if I have sleep)")
    print("6. Staying up late at night to finish projects")
    print_border()
    return_to_main_menu()

def random_fact():
    fact = "Did you know that turtles can breathe through their butts?"
    print("RANDOM FACTS:")
    print_border()
    print("Do you want to know a random fact?")

    while True:
        user_input = input("Answer with 'yes' or 'no': ").strip().lower()
        print_border()

        if user_input == 'yes':
            print(fact)
            break
        elif user_input == 'no':
            second_input = input("Nope, try again! "
                                    + "'yes' or 'no': ").strip().lower()
            print_border()
            if second_input == 'yes':
                print(fact)
            elif second_input == 'no':
                print("Awww fine. Maybe next time!")
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")
            break
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

    print_border()
    return_to_main_menu()

def comment_section(comment_id):
    comments = {
        '5': "COMMENT FROM CAUSON:\n", #TODO(Causon): Add comment here
        '6': "COMMENT FROM EFONDO:\n", #TODO(Efondo): Add comment here
        '7': "COMMENT FROM GAGTAN:\n", #TODO(Gagtan): Add comment here
        '8': "COMMENT FROM LOPEZ:\n"   #TODO(Lopez): Add comment here
    }

    title = comments.get(comment_id, "No comment available.")
    print(title)
    print_border()
    return_to_main_menu()

# Menu logic
def franco_main():
    menu_options = {
        '1': basic_information,
        '2': goals,
        '3': skills,
        '4': random_fact,
        '5': lambda: comment_section('5'),
        '6': lambda: comment_section('6'),
        '7': lambda: comment_section('7'),
        '8': lambda: comment_section('8')
    }

    while True:
        clear_screen()
        print("Hello there, I am Fernette Pearl Franco!")
        print_border()
        print("1. Basic Information")
        print("2. Goals")
        print("3. Skills")
        print("4. A Random Fact")
        print("5. Comment from Causon")
        print("6. Comment from Efondo")
        print("7. Comment from Gagtan")
        print("8. Comment from Lopez")
        print("9. Exit")
        print_border()

        choice = input("Please select an option (1-9): ")

        if choice == '9':
            print("Thank you for visiting! Goodbye!")
            break
        elif choice in menu_options:
            display_section(menu_options[choice])
        else:
            print("Invalid choice. Please select a number between 1 and 9.")
            return_to_main_menu()

franco_main()
