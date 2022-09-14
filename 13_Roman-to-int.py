def RomanToInt(s: str):
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    str_s = list(s)
    n = len(str_s)
    value = 0
    for i in str_s:
        value += r_dict[i]
        print(value)


if __name__ == "__main__":
    print(RomanToInt('III'))
    print(RomanToInt("LVIII"))
    print(RomanToInt("MCMXCIV"))
