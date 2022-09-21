# Write a program that generates a random number and asks the user to guess what the number is. If the user's guess
# is higher than the random number, the program should display "Too high, try again." If the user's guess is lower
# than the random number, the program should display "Too low, try again." The program should use a loop that repeats
# until the user correctly guesses the random number.
import random


def random_number():
    rand = random.randint(1, 10)
    i = "1"
    while i == "1":
        n = int(input("Choice number between 1 t0 10 : "))
        if n < rand:
            print("Too low, Try again")
        elif n > rand:
            print("Too high, Try again")
        else:
            print("Correct Answer")
            break
        i = "0"
        i = input("Continue press 1 or for end :")


if __name__ == "__main__":

    random_number()
