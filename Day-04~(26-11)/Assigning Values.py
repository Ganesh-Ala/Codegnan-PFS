print("assigning Multiple Values to Multiple Variables.")
num1, num2, num3 = 10, 20, 30
print("Number 1: ", num1)
print("Number 2: ", num2)
print("Number 3: ", num3)
print("All Numbers: ", id(num1), id(num2), id(num3))

print("assigning Single Values to Multiple Variables.")
num1, num2, num3 = 10, 10, 10
print("Number 1: ", num1)
print("Number 2: ", num2)
print("Number 3: ", num3)
print("All Numbers: ", id(num1), id(num2), id(num3))

print("assigning Multiple Values to Multiple Variables.")
num1, num2, num3 = 355, 355, 355
print("Number 1: ", num1)
print("Number 2: ", num2)
print("Number 3: ", num3)
print("All Numbers: ", id(num1), id(num2), id(num3))
print()

print("Swapping Two Numbers:")
a, b = 10, 20
print("Before Swapping:", a, b)
a, b = b, a
print("After Swapping:", a, b)
