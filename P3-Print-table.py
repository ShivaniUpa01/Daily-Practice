# Write a program that prompts the user to input a positive integer. It should then print the multiplication table of
# that number.
def print_table(n):
    for i in range(1, 11):
        mul = i * n
        print("%d * %d  = %d" % (n, i, mul))


if __name__ == "__main__":
    print("Print the table of a  given number: ")
    num = int(input())
    print_table(num)
