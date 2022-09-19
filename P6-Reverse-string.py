# Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For
# example, if the input is 12345, the output should be 54321.
def reverse(num):
    rem = 0
    result = 0
    while num != 0:
        rem = int(num % 10)
        num = int(num / 10)
        result = 10 * result + rem
    print(result)


if __name__ == "__main__":
    n = int(input("Enter big number for reverse : "))
    reverse(n)
