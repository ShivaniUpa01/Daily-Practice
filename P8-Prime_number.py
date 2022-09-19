# Write a program that prompts the user to input a positive integer. It should then output a message indicating whether
# the number is a prime number.
def prime(n):
    p = 0
    for i in range(2, n):
        p = n % i
        if p == 0:
            print("Number is a not prime ")
            break
        else:
            print("number is prime")
            break


if __name__ == "__main__":
    num = int(input("Enter a number to find prime : "))
    prime(num)
