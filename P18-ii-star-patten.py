""" Write a program to print following:
ii)
    *
    **
    ***
    ****
    *****  """


def star_pattern_ii(m):
    for j in range(m + 1):
        p = "*"
        print(p * j)


"""
iii)
    *
   **
  ***
 ****
*****
"""


def pattern_iii(n):
    for i in range(n + 1):
        print((" " * (n - i)) + ("*" * i))


"""iv)
        *
      ***
    *****
  *******
*********"""


def pattern_iv(n):
    for i in range(n + 1):
        print((" " * (n - i)) + ("*" * (i + 1)) + ("*" * i) + (" " * (n - i)))


"""
v)
        1
       222
      33333
     4444444
    555555555 """


def pattern_v(n):
    for i in range(1, n + 1):
        print((" " * (n - i)) + (str(i) * i + (str(i) * (i - 1)) + (" " * (n - i))))


"""
vi)
        1
       212
      32123
     4321234
    543212345"""


def pattern_vi(n):
    for i in range(1, n+1):
        num = ""
        for j in range(1, i+1):
            # print(n-j ,end="")
            num += str(j)
            # print((str(j)), end="")

        num = num[::-1]+num[1:]
        print((" " * (n-i)) + num + (" " * (n-i)))



pattern_vi(5)
pattern_v(5)
pattern_iv(5)
star_pattern_ii(5)
pattern_iii(5)
