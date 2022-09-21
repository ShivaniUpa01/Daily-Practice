# Compute the natural logarithm of 2, by adding up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where
# n is a positive integer and input by user.
def rational_number(n):
    add = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            add += (1 / i) * -1
        else:
            add += 1 / i
        print("add %.2f " % add)


rational_number(10)
