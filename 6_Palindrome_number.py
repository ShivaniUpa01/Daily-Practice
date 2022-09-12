def palindrome_num(x):
    print(x, end=" == ")

    str_x = str(x)
    n = str_x[::-1]
    if n == str_x:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    palindrome_num(121)
    palindrome_num(123)
    palindrome_num(-121)
