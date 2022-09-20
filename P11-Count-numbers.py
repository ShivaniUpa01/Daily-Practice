# Write a program to enter the numbers till the user wants and at the end it should display the count of positive,
# negative and zeros entered.
def count_all_number():
    i = "1"
    count = ""
    while i == "1":
        num = int(input("Number : "))
        count = count + str(num)
        print(count)
        i = "0"
        i = input("Continue if yes press 1 for no press 0 : ")


if __name__ == "__main__":
    count_all_number()
