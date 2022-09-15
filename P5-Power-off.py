# Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power
# of another. (Do not use built-in method)


def power_of_number(n, p):
    mul = 1
    for i in range(1, p + 1):
        mul *= n
    print(mul)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    p = int(input("Enter a power: "))

    power_of_number(n, p)
