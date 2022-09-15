# Write a program to find the factorial value of any number entered through the keyboard.
def factorial_number(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        print(fact)
    return fact


if __name__ == "__main__":
    numbers = int(input("Give a number for factorial : "))
    print(factorial_number(numbers))
