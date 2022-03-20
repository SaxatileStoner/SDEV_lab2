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
"""
from calendar import c
from logging import exception
from multiprocessing.sharedctypes import Value
import secrets
import math
import random
import datetime
import string

from pip import main

global option
option = ['a', 'b', 'c', 'd', 'e', 'f']
# default option array


def validate_single_user_input(user_input, acceptable=option):
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


def validate_array_user_input(user_input, acceptable=option):
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
    print("\na. Must use an UPPERCASE letter\n" +
          "b. Must use a lowercase letter\n" +
          "c. Must use a number (0-9) character\n" +
          "d. Must use a special character\n")
    # NOTE, could make a default e. option


def gen_password():
    """Promts user for the length of the password as well as complexity (Use of Upper, Lower, Numbers, and Special Characters)
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
            else:
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


def __main__():

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
        if option[0] == user_selection:
            # Perform function for a
            print(f"Your password is: {gen_password()}\n")
        elif option[1] == user_selection:
            # Perform function for b
            print("temp")
        elif option[2] == user_selection:
            # Perform function for c
            print("temp")
        elif option[3] == user_selection:
            # Perform function for d
            print("temp")
        elif option[4] == user_selection:
            # Perform function for e
            print("temp")
        elif option[5] == user_selection:
            # Perform function for f
            print("\tGoodbye!")
            return 0
        else:
            print("Error! Well, don't know how you got here?")


__main__()
