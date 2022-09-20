# Write a program to enter the numbers till the user wants and at the end the program should display the largest and
# smallest numbers entered.
def find_large_small_int(n):
    mini = float('inf')
    maxi = float("-inf")
    for i in n:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    print("Minimum : ", mini)
    print("Maximum : ", maxi)


if __name__ == "__main__":
    num = list(map(int, input("enter the number : ").split()))
    find_large_small_int(num)
