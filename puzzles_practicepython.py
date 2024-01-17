<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
from random import choice, randint
from time import time
import string
from werkzeug.security import generate_password_hash
from bs4 import BeautifulSoup
import requests


# List comprehensions
def puzzle1():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    a_even = [num for num in a if num % 2 == 0]
    print(a_even)

# puzzle1()


# Rock, paper, scissors
def puzzle2():
    choice_user = ""
    while choice_user != "quit":
        result = ""
        choices = ["rock", "paper", "scissors"]
        choice_user = input("Choose rock, paper, or scissors (quit the game by typing 'quit'): ")
        choice_comp = choice(choices)
        match choice_user:
            case "rock":
                if choice_comp == "rock":
                    result = "DRAW"
                elif choice_comp == "paper":
                    result = "COMP WINS"
                else:
                    result = "YOU WIN"
            case "paper":
                if choice_comp == "rock":
                    result = "YOU WIN"
                elif choice_comp == "paper":
                    result = "DRAW"
                else:
                    result = "COMP WIN"
            case "scissors":
                if choice_comp == "rock":
                    result = "COMP WINS"
                elif choice_comp == "paper":
                    result = "YOU WIN"
                else:
                    result = "DRAW"
        print(result)

# puzzle2()


# Fibonacci sequence
def puzzle3():
    length = int(input("Select length of the Fibonacci sequence: "))
    sequence = []
    for i in range(length):
        if i < 2:
            sequence.append(1)
        else:
            sequence.append(sequence[-2] + sequence[-1])
    print(sequence)


# puzzle3()


# Password generator
def puzzle4():
    chars_lower = list(string.ascii_lowercase)
    chars_upper = list(string.ascii_uppercase)
    numbers = list(string.digits)
    specials = list(string.punctuation)
    length = int(input("Length of your password: "))
    security = int(input("Choose the level of security (1-4): "))
    password = ""
    for char in range(length):
        match security:
            case 1:
                char = choice(chars_lower)
                password += char
            case 2:
                char = choice(chars_lower + chars_upper)
                password += char
            case 3:
                char = choice(chars_lower + chars_upper + numbers)
                password += char
            case 4:
                if password == "":
                    char = choice(chars_lower + chars_upper + numbers)
                else:
                    char = choice(chars_lower + chars_upper + numbers + specials)
                password += char
    with open("passwords.txt", "a") as file:
        file.write(password + " >>> HASH: " + generate_password_hash(password) + "\n")
    print(password)

# puzzle4()


# Extract web information
def puzzle5():
    url = "https://respekt.cz/"
    raw = requests.get(url)
    raw_html = raw.text
    raw_soup = BeautifulSoup(raw_html, "lxml")
    for heading in raw_soup.find_all("h2"):
        try:
            if "ArticlePreview_heading" in heading["class"][0]:
                print(f"+ {heading.string}\n")
        except KeyError:
            continue

# puzzle5()


# Guess a number ala MasterMind
# def puzzle6():
#     print("Welcome to the Cows & Bulls game!")
#     num = str(randint(1000, 9999))
#     guess = "0"
#     bulls = 0
#     cows = 0
#     tries = 0
#     print(num)
#     while guess != num:
#         guess = input("Enter a number (4 digits): ")
#         for i in range(len(guess)):
#             if guess[i] == num[i]:
#                 bulls += 1
#                 num_temp = num.replace(num[i], "x")
#             elif guess[i] in num_temp:
#                 cows += 1
#         print(f"Cows: {cows}, Bulls: {bulls}")
#         cows = 0
#         bulls = 0
#         tries += 1
#     print(f"Congratulations! You've guessed the number in {tries} tries.")

# puzzle6()


# Computer guesses player's number!
def puzzle7():
    numbers = list(range(101))
    median = lambda: int(len(numbers)/2)
    user_num = -1
    guess = numbers[median()]
    tries = 0
    while user_num != guess:
        print(guess)
        num_rel = input("Is your number greater (g), smaller (s), or equal (e)? ")
        if num_rel == "g":
            for number in numbers[:numbers.index(guess)]:
                numbers.remove(number)
            guess = numbers[median()]
        elif num_rel == "s":
            for number in numbers[numbers.index(guess):]:
                numbers.remove(number)
            guess = numbers[median()]
        elif num_rel == "e":
            user_num = guess
        else:
            continue
        tries += 1
    print(f"Computer guessed your number {user_num} in {tries} tries.")

# puzzle7()


# Grid making
def puzzle8():
    size = int(input("Row length: "))
    make_grid(size)

def make_grid(size):
    for i in range(size):
        print(" ---" * size)
        print("|   " * size, end="|\n")
    print(" ---" * size)

puzzle8()

<<<<<<< HEAD
=======
=======
from random import choice, randint
from time import time
import string
from werkzeug.security import generate_password_hash
from bs4 import BeautifulSoup
import requests


# List comprehensions
def puzzle1():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    a_even = [num for num in a if num % 2 == 0]
    print(a_even)

# puzzle1()


# Rock, paper, scissors
def puzzle2():
    choice_user = ""
    while choice_user != "quit":
        result = ""
        choices = ["rock", "paper", "scissors"]
        choice_user = input("Choose rock, paper, or scissors (quit the game by typing 'quit'): ")
        choice_comp = choice(choices)
        match choice_user:
            case "rock":
                if choice_comp == "rock":
                    result = "DRAW"
                elif choice_comp == "paper":
                    result = "COMP WINS"
                else:
                    result = "YOU WIN"
            case "paper":
                if choice_comp == "rock":
                    result = "YOU WIN"
                elif choice_comp == "paper":
                    result = "DRAW"
                else:
                    result = "COMP WIN"
            case "scissors":
                if choice_comp == "rock":
                    result = "COMP WINS"
                elif choice_comp == "paper":
                    result = "YOU WIN"
                else:
                    result = "DRAW"
        print(result)

# puzzle2()


# Fibonacci sequence
def puzzle3():
    length = int(input("Select length of the Fibonacci sequence: "))
    sequence = []
    for i in range(length):
        if i < 2:
            sequence.append(1)
        else:
            sequence.append(sequence[-2] + sequence[-1])
    print(sequence)


# puzzle3()


# Password generator
def puzzle4():
    chars_lower = list(string.ascii_lowercase)
    chars_upper = list(string.ascii_uppercase)
    numbers = list(string.digits)
    specials = list(string.punctuation)
    length = int(input("Length of your password: "))
    security = int(input("Choose the level of security (1-4): "))
    password = ""
    for char in range(length):
        match security:
            case 1:
                char = choice(chars_lower)
                password += char
            case 2:
                char = choice(chars_lower + chars_upper)
                password += char
            case 3:
                char = choice(chars_lower + chars_upper + numbers)
                password += char
            case 4:
                if password == "":
                    char = choice(chars_lower + chars_upper + numbers)
                else:
                    char = choice(chars_lower + chars_upper + numbers + specials)
                password += char
    with open("passwords.txt", "a") as file:
        file.write(password + " >>> HASH: " + generate_password_hash(password) + "\n")
    print(password)

# puzzle4()


# Extract web information
def puzzle5():
    url = "https://respekt.cz/"
    raw = requests.get(url)
    raw_html = raw.text
    raw_soup = BeautifulSoup(raw_html, "lxml")
    for heading in raw_soup.find_all("h2"):
        try:
            if "ArticlePreview_heading" in heading["class"][0]:
                print(f"+ {heading.string}\n")
        except KeyError:
            continue

# puzzle5()


# Guess a number ala MasterMind
# def puzzle6():
#     print("Welcome to the Cows & Bulls game!")
#     num = str(randint(1000, 9999))
#     guess = "0"
#     bulls = 0
#     cows = 0
#     tries = 0
#     print(num)
#     while guess != num:
#         guess = input("Enter a number (4 digits): ")
#         for i in range(len(guess)):
#             if guess[i] == num[i]:
#                 bulls += 1
#                 num_temp = num.replace(num[i], "x")
#             elif guess[i] in num_temp:
#                 cows += 1
#         print(f"Cows: {cows}, Bulls: {bulls}")
#         cows = 0
#         bulls = 0
#         tries += 1
#     print(f"Congratulations! You've guessed the number in {tries} tries.")

# puzzle6()


# Computer guesses player's number!
def puzzle7():
    numbers = list(range(101))
    median = lambda: int(len(numbers)/2)
    user_num = -1
    guess = numbers[median()]
    tries = 0
    while user_num != guess:
        print(guess)
        num_rel = input("Is your number greater (g), smaller (s), or equal (e)? ")
        if num_rel == "g":
            for number in numbers[:numbers.index(guess)]:
                numbers.remove(number)
            guess = numbers[median()]
        elif num_rel == "s":
            for number in numbers[numbers.index(guess):]:
                numbers.remove(number)
            guess = numbers[median()]
        elif num_rel == "e":
            user_num = guess
        else:
            continue
        tries += 1
    print(f"Computer guessed your number {user_num} in {tries} tries.")

# puzzle7()


# Grid making
def puzzle8():
    size = int(input("Row length: "))
    make_grid(size)

def make_grid(size):
    for i in range(size):
        print(" ---" * size)
        print("|   " * size, end="|\n")
    print(" ---" * size)

puzzle8()

>>>>>>> 1c4bb1d554e1787639bd741b2ae2402151fd51a2
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
