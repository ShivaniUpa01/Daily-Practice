# Write a program to calculate the sum of following series where n is input by user. 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/n
def rational_number(n):
    add = 0
    for i in range(1, n+1):
        add += 1 / i
    print("add : %.2f" % add)


if __name__=="__main__":
    num = int(input("enter number : "))
    rational_number(num)
