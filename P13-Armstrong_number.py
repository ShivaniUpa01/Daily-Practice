# Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number
# is equal to the number itself, then the number is called an Armstrong number.
# For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )
def armstrong_num():
    n = 500
    for i in range(0, n+1):
        arm = 0
        for j in str(i):
            arm = int(j) ** 3 + arm
        if arm == i:
            print(arm)


# if __name__ == "__main__":
#     num = input("Enter a number : ")
#     armstrong_num(num)
print(armstrong_num())
