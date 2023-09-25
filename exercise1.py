import math

## 1 Print your name.
myname = input("What is your name?: ")
print("Hello, " + myname + "!")
print("----------------------------------------------------------------------")

# 2 Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius = float(input("Import the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of the circle with radius {radius:.2f} is {area:.3f}")
print("----------------------------------------------------------------------")

# 3 Write a program that ask the user for the length and width of a rectangle. The program then prints out the perimeter and area of the circle.
# Ask the user for the input
length = float(input("The length of the rectangle: "))
width = float(input("The width of the rectangle: "))
# Calculating
perimeter = 2 * (length + width)
area = length * width
# Print out the results
print(f"The perimeter of the rectangle is {perimeter}")
print(f"The area of the rectangle is {area}")
print("----------------------------------------------------------------------")

# 4 Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the number.
num1 = int(input("The first integer: "))
num2 = int(input("The second integer: "))
num3 = int(input("The third integer: "))
# Calculate
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
# Print out the results
print(f"The sum of the numbers is {sum}")
print(f"The product of the numbers is {product}")
print(f"The average of the numbers is {average}")
print("----------------------------------------------------------------------")

# 5 Write a program that ask the user to enter a mass in medieval unit: talents, pounds, and lots. The program converts the input to full kilograms and grams and outputs the result to the user.
# One talent is 20 pounds. One pounds is 32 lots and One lot is 13,3 grams.=
# Ask the user the input
talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
lots = float(input("Enter the mass in lots: "))
# Define conversion factors
TalentToPound = 20
PoundToLots = 32
LotstoGrams = 13.3
# Convert
total_grams = ((((talents * TalentToPound) + pounds) * PoundToLots) + lots) * LotstoGrams
kilogram = total_grams // 1000
gram = total_grams - kilogram * 1000
# Print out the results
print(f"The mass is approximately {kilogram:.1f} kilograms and {gram:.2f} grams.")

