# Write a program to calculate HCF of Two given number.
def hcf_num(n):
    for i in range(2, n):
        if n % i == 0:
            hcf = int(n / i)
            print(hcf)

hcf_num(12)
