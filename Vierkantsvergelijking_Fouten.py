import math

print("This program solves a quadratic equation of the form 'ax^2 + bx + c = 0'")
print("Please enter the coefficients a, b, and c.")

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4 * a * c

print("Root 1: {root1}\nRoot 2: {root2"}

if discriminant > 0
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant) / (2 * a)
    print(f"Root 1: {root1}\nRoot 2: {root2}

elif discriminant == 0
    root = -b / (2 * a)
    print(f"Root: {root}

else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"Root 1: {root1}\nRoot 2: {root2}
