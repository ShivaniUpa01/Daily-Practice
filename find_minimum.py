def find_minimum(input_list):
    value = 1000000
    index = -1
    for i in range(len(input_list)):
        if input_list[i] < value:
            value = input_list[i]
            index = i
    return value


if __name__ == "__main__":
    given_list = [8, 6, 15, 4, 10]
    print("Minimum value of the list ", find_minimum(given_list))


