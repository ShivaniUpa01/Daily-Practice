def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total


def factorial(x):
  fact = 1
  for i in range(x, 1, -1):
    fact =fact * i
  return fact
