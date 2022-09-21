""" Write a program to print following:
i) 
    **********
    **********
    **********
    ********** """


def star_matrix(n, m):
    for i in range(n):
        for j in range(m):
            print("*", end=" ")
        print("")


star_matrix(5, 7)
