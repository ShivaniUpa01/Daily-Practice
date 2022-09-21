# Write a program to print Fibonacci series of n terms where n is input by user : 0 1 1 2 3 5 8 13 24 .....
def fibonacci_series(n):
    first = 0
    second = 1
    fab = 1
    for i in range(n):
        if i == 0:
            fab = 0
        elif i == 1:
            fab = 1
        else:
            fab = first + second
            first = second
            second = fab
        print("N = " + str(i) +"-----"+str(fab))


fibonacci_series(11)
