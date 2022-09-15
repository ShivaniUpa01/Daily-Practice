# Write a program to print numbers from 1 to 10.
def count_num(num):
    for i in range(1, num + 1):
        print(i, end=" ")


if __name__ == "__main__":
    # print(count_num(50)) it show none at end
    count_num(50)
