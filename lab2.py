"""
* Building Secure Python Apps - SDEV 300
* Lab 2
* @author Christopher Stoner
* @date 30 Mar 2022
*
* Create a menu-driven python application with following menu options:
*       a. Generate Secure Password
*       b. Calculate and Format a Percentage
*       c. How many days from today until July 4, 2025?
*       d. Use the Law of Cosines to calculate the leg of a triangle.
*       e. Calculate the volume of a Right Circular Cylinder
*       f. Exit program
* TODO, Document testing result into test_cases_pylint.docx
* TODO, Run Pylint an make any needed changes after running
"""

import secrets
import math
import datetime
import string

global OPTION
OPTION = ['a', 'b', 'c', 'd', 'e', 'f']
# default option array


def validate_single_user_input(user_input, acceptable=OPTION):
    """Used to check if the user has made a SINGLE valid choice with the printed menu

    Args:
        user_input (str): Input from the user about the menu selection made
        acceptable_input_array (str_array): The array of topions that are considered acceptable

    Returns:
        bool: True means that the user has inputted a valid character for the menu selection
              False means that the user has inputted a NON-VALID character for the menu selection
    """
    for i in acceptable:
        if user_input == i:
            return True
    return False


def validate_array_user_input(user_input, acceptable=OPTION):
    """Used to check if the user has made a valid ARRAY of choices with the printed menu

    Args:
        user_input (str_array): User input array if multiple choices are expected
        acceptable_array (str_array, optional): Array of choices. Defaults to option.

    Returns:
        bool: True when ALL choices are of the acceptable array
              False when a single choice is NOT of the acceptable array
    """
    user_input = list(user_input)
    # Strips all whitespace chars
    user_input = [i for i in user_input if i.strip()]
    acceptable = list(acceptable)
    counter = 0
    for acceptable_element in acceptable:
        for user_element in user_input:
            if acceptable_element == user_element:
                counter += 1
    if counter == user_input.__len__():
        return True
    return False


def process_array_input(user_input):
    """Puts a user's str input into a list that is seperated
    by whitespace into a list, strips the whitespace,
    removes repeats, and sorts the list alphabetically

    Args:
        user_input (str): string to be operated on
        and returned

    Returns:
        list: stripped, removed repeats, and sortted list
        from user_input
    """
    user_input = list(user_input)  # Convert str to list
    user_input = [i for i in user_input if i.strip()]  # Strip Whitespace
    user_input = [i for n, i in enumerate(
        user_input) if i not in user_input[:n]]  # Remove Dups
    user_input = sorted(user_input)
    return user_input


def print_menu():
    """Prints out menu option for the user to select
    """
    print("a. Generate Secure Password\n" +
          "b. Calculate and Format a Percentage\n" +
          "c. How many days from today until July 4, 2025?\n" +
          "d. Use the Law of Cosines to calculate the leg of a triangle\n" +
          "e. Calculate the volume of a Right Circular Cylinder\n" +
          "f. Exit program\n")


def print_password_menu():
    """Prints the password menu
    """
    print("\na. Must use an UPPERCASE letter\n" +
          "b. Must use a lowercase letter\n" +
          "c. Must use a number (0-9) character\n" +
          "d. Must use a special character\n")


def gen_password():
    """Generates a password through a series of promts

    Returns:
        str: Password
    """
    acceptable = ['a', 'b', 'c', 'd']
    print("\nWelcome to the password generator Python application!\n" +
          "Please make your selection below for your password!\n" +
          "(For multiple selections, type your selection\n" +
          "followed by a space for the next.")
    print_password_menu()
    user_selection = input()
    while not validate_array_user_input(user_selection, acceptable):
        print("\tNot a Valid Selection!\n")
        print_password_menu()
        user_selection = input()

    # Process given str into a stripped, non-redundant, sorted list
    user_selection = process_array_input(user_selection)

    # Determine how LONG the user wants this password to be
    while True:
        try:
            print("\nHow long would you like this password? 8-256 characters long")
            pass_len = int(input())
            if pass_len >= 8 and pass_len <= 256:
                break  # The user input is a valid int AND is between 8-256 characters
            print("\nMUST be between 8-256 characters!")
            continue
        except ValueError:
            print("\nThat is NOT a valid integer!")
            continue

    # Determine how many of each character type
    min_avaliable = pass_len
    min_uppercase_letters = 0
    min_lowercase_letters = 0
    min_num_chars = 0
    min_spec_chars = 0
    if user_selection.__contains__('a'):
        while True:
            try:
                print("\nWhat is the min amount of UPPERCASE letters?")
                min_uppercase_letters = int(input())
                if min_uppercase_letters >= min_avaliable:
                    print("\nmin cannot be the same or greater than pass length!")
                    print(f"Your min avaliable is: {min_avaliable}")
                    continue
                min_avaliable -= min_uppercase_letters
                break
            except ValueError:
                print("\nThat is NOT a valid integer!")
                continue
    if user_selection.__contains__('b'):
        while True:
            try:
                print("\nWhat is the min amount of lowercase letters?")
                min_lowercase_letters = int(input())
                if min_lowercase_letters >= min_avaliable:
                    print("\nmin cannot be the same or greater than pass length!")
                    print(f"Your min avaliable is: {min_avaliable}")
                    continue
                min_avaliable -= min_uppercase_letters
                break
            except ValueError:
                print("\nThat is NOT a valid integer!")
                continue
    if user_selection.__contains__('c'):
        while True:
            try:
                print("\nWhat is the min amount of number characters?")
                min_num_chars = int(input())
                if min_num_chars >= min_avaliable:
                    print("\nmin cannot be the same or greater than pass length!")
                    print(f"Your min avaliable is: {min_avaliable}")
                    continue
                min_avaliable -= min_num_chars
                break
            except ValueError:
                print("\nThat is NOT a valid integer!")
                continue
    if user_selection.__contains__('d'):
        while True:
            try:
                print("\nWhat is the min amount of special characters?")
                min_spec_chars = int(input())
                if min_spec_chars >= min_avaliable:
                    print("\nmin cannot be the same or greater than pass length!")
                    print(f"Your min avaliable is: {min_avaliable}")
                    continue
                min_avaliable -= min_spec_chars
                break
            except ValueError:
                print("\nThat is NOT a valid integer!")
                continue

    # min amounts aquired, now to turn into a list for further processing
    min_amounts = [min_uppercase_letters,
                   min_lowercase_letters,
                   min_num_chars,
                   min_spec_chars]

    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet)
                           for i in range(0, pass_len))
        if sum(j.isupper() for j in password) >= min_amounts[0] and \
                sum(j.islower() for j in password) >= min_amounts[1] and \
                sum(j.isdigit() for j in password) >= min_amounts[2] and \
                sum(j in string.punctuation for j in password) >= min_amounts[3]:
            break

    return password


def gen_percentage():
    """Divide by promtted numerator and denominator, can use
    return to format as a percent

    Returns:
        float: Quotient of numerator and denominator
    """
    print("\nInput your numerator: ")
    while True:
        try:
            numerator = float(input())
            break
        except ValueError:
            print("MUST be a float value!")
            continue

    print("\nInput your denominator: ")
    while True:
        try:
            denominator = float(input())
            if denominator == 0:
                print("Denominator CANNOT be 0!")
                continue
            break
        except ValueError:
            print("MUST be a float value!")
            continue

    return numerator/denominator


def calc_days_between():
    """returns the amount of days between today and 4 July 2025

    Returns:
        timedelta: Day difference between today and 4 July 2025
    """
    return datetime.date(2025, 7, 4) - datetime.date.today()


def calc_leg_triangle():
    """Uses the law of cos to find the missing value of side C
    LAW OF COS: c^2 = a^2 + b^2 - 2ab*cos(C)

    Returns:
        float: The value of side C from inputs a, b, angle c
    """
    print("\nThe Law of Cosines: c^2 = a^2 + b^2 - 2ab*cos(C)")
    # We need to get a, b, and big C from the user
    while True:
        try:
            side_a = float(input("\nEnter Value for 'Side A': "))
            if side_a > 0:
                break
            print("\nValue 'Side A' MUST be greater than 0!")
            continue
        except ValueError:
            print("Value 'Side A' MUST be a float value type!")

    while True:
        try:
            side_b = float(input("\nEnter Value for 'Side B': "))
            if side_b > 0:
                break
            print("\nValue 'Side B' MUST be greater than 0!")
            continue
        except ValueError:
            print("Value 'Side B' MUST be a float value type!")

    while True:
        try:
            angle_c = float(input("\nEnter Value for 'Angle C': "))
            if angle_c > 0:
                break
            print("\nValue 'Angle C' MUST be greater than 0!")
            continue
        except ValueError:
            print("Value 'Angle C' MUST be a float value type!")

    return math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2) -
                     2*side_a*side_b*math.cos(math.radians(angle_c)))


def calc_vol_circular_cylinder():
    """Finds the volume in measurements of units of a right circular cylinder
    V = (pi*r^2) * Height
    """
    print("\nVolume of Circular Cylinder = (pi*r^2) * h")
    # We need to aquire values r and height from the user
    while True:
        try:
            radius = float(input("\nEnter Value for 'Radius': "))
            if radius > 0:
                break
            print("\nValue 'Radius' MUST be greater than 0!")
            continue
        except ValueError:
            print("Value 'Radius' MUST be a float value type!")

    while True:
        try:
            height = float(input("\nEnter Value for 'Height': "))
            if height > 0:
                break
            print("\nValue 'Height' MUST be greater than 0!")
            continue
        except ValueError:
            print("Value 'Height' MUST be a float value type!")

    return (math.pi * math.pow(radius, 2)) * height


def __main__():
    """Main Program to call

    Returns:
        int: returns 0 for normal function exit
    """
    print("Hello, Welcome to the Lab 2 Program! Please make a selection from the below menu:")
    while True:
        print_menu()
        user_selection = input()
        while not validate_single_user_input(user_selection):
            print("\tNot a Valid Selection!\n")
            print_menu()
            user_selection = input()

        # User input has been validated to be
        # one of the allowed options.
        if OPTION[0] == user_selection:
            # Perform function for a
            print(f"Your password is: {gen_password()}\n")
        elif OPTION[1] == user_selection:
            # Perform function for b
            print(f"{gen_percentage():.2%}\n")
        elif OPTION[2] == user_selection:
            # Perform function for c
            print(f"Days until 4 July, 2025: {calc_days_between()}\n")
        elif OPTION[3] == user_selection:
            # Perform function for d
            print(f"Value for Side C is: {calc_leg_triangle():.3}\n")
        elif OPTION[4] == user_selection:
            # Perform function for e
            print(
                f"Volume of Circular Cylinder = {calc_vol_circular_cylinder():.3}\n")
        elif OPTION[5] == user_selection:
            # Perform function for f
            print("\tGoodbye!")
            return 0
        else:
            print("Error! Well, don't know how you got here?")


__main__()
