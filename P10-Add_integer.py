# Write a do-while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed.
# The loop should ask the user whether he or she wishes to perform the operation again. If so, the loop should
# repeat; otherwise it should terminate
def add_num():
    i = "1"
    while i == "1":
        n = int(input("Enter first number : "))
        m = int(input("Enter second number : "))
        add = int(n + m)
        print(add)
        i = "0"
        i = str(input("If Continue the enter 1 or not enter 0 : "))


if __name__ == "__main__":
    add_num()
