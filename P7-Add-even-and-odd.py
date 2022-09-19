# Write a program that reads a set of integers, and then prints the sum of the even and odd integers.
def sum_int(n):
    rem = 0
    even = 0
    odd = 0
    while n != 0:
        rem = int(n % 10)
        n = int(n / 10)
        if rem % 2 == 0:
            even += rem
        else:
            odd += rem
    print(even, odd)


if __name__ =="__main__":
    num = int(input("Enter the long digit number : "))
    sum_int(num)
