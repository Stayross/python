import math

side_a = float(input("Enter the length of the first perpendicular side (a): "))
side_b = float(input("Enter the length of the second perpendicular side (b): "))


hypotenuse_squared = side_a**2 + side_b**2


hypotenuse = math.sqrt(hypotenuse_squared)


if hypotenuse.is_integer():
    print(f"The hypotenuse is: {int(hypotenuse)}")
else:
    print(f"The hypotenuse is: √{hypotenuse_squared}")
    print(f"(Approximately: {hypotenuse:.4f})")