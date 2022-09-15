# Write a program in Python to calculate the volume of a sphere.
# Hint
# Your function should start with something like def volume(r).  i.e. radius
# value of r should be 2
#
# Expected Output
# 4071.5040790523717
def volume_of_sphere(radius):
    vos = 4 / 3 * 3.14159 * radius ** 3
    # vos = ((4 * 3.14159 * radius ** 3) / 3)
    return vos


if __name__ == "__main__":
    print(volume_of_sphere(2))