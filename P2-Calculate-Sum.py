# Write a program to calculate the sum of first 10 natural number.
def cal_sum(num):
    n = 0
    for i in range(0, num):
        n += i
    return n


if __name__ == "__main__":
    print(cal_sum(10))
