import random

# 3 Conditional structures (if)
# 3.1 Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.
sizeLimit = 42
zanderLength = float(input("Enter the length of the zander in centimeters: "))
if zanderLength >= sizeLimit:
    print("Congratulations! You can keep the zander.")
else:
    notify = sizeLimit - zanderLength
    print(f"The zander is {notify:.2f} centimeters below the size limit.")
    print("Please release the fish back into the lake.")
    print("-------------------------------------------------------------------------------------------------")

# 3.2 Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")
if cabin_class == "LUX":
    print("You have selected a LUX cabin: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("You have selected an A cabin: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("You have selected a B cabin: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("You have selected a C cabin: windowless cabin below the car deck.")
else:
    print("Invalid cabin class. Please enter LUX, A, B, or C.")
print("-------------------------------------------------------------------------------------------------")

# 3.3 Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

biologicalGender = input("male/female: ").strip().lower()
normalRangeMale = [134, 167]
normalRangeFemale = [117, 155]
hemoglobin = float(input("your hemoglobin is: "))
if biologicalGender == "female":
    if hemoglobin < normalRangeFemale[0]:
        print("Your hemoglobin value is low.")
    elif normalRangeFemale[0] <= hemoglobin <= normalRangeFemale[1]:
        print("Your hemoglobin value is within the normal range.")
    else:
        print("Your hemoglobin value is high.")
if biologicalGender == "male":
    if hemoglobin < normalRangeMale[0]:
        print("Your hemoglobin value is low.")
    elif normalRangeMale[0] <= hemoglobin <= normalRangeMale[1]:
        print("Your hemoglobin value is within the normal range.")
    else:
        print("Your hemoglobin value is high.")

print("-------------------------------------------------------------------------------------------------")

# 3.4 Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.
# Ask the user to enter a year
year = int(input("Enter a year: "))
# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0 and year % 400 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("-------------------------------------------------------------------------------------------------")

# 4 While loop

# 4.1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
print("-------------------------------------------------------------------------------------------------")

# 4.2 Define the conversion factor from inches to centimeters
inchToCentimeters = 2.54
while True:
    inches = float(input("Enter a length in inches (or a negative value to exit): "))
    if inches < 0:
        print("Program has ended.")
        break
    centimeters = inches * inchToCentimeters
    print(f"{inches} inches is equal to {centimeters} centimeters.")
print("-------------------------------------------------------------------------------------------------")

# 4.3 Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
numbers = []
while True:
    userInput = input("Enter a number (or press Enter to quit): ")
    if userInput == "":
        break
    try:
        number = float(userInput)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if numbers:
    print("No numbers entered.")
else:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
print("-------------------------------------------------------------------------------------------------")

# 4.4 Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

correctNum = random.randint(1, 10)
while True:
    guessNum = int(input("Guess the number between 1 and 10: "))
    if guessNum < correctNum:
        print("Too low!")
    elif guessNum > correctNum:
        print("Too high!")
    else:
        print("Correct!")
        break
print("-------------------------------------------------------------------------------------------------")
# 4.5 Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.
correctUsername = "python"
correctPassword = "rules"
maxAttempts = 5
attempts = 0
while attempts < maxAttempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correctUsername and password == correctPassword:
        print("Welcome.")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1
if attempts == maxAttempts:
    print("Access denied.")
print("-------------------------------------------------------------------------------------------------")
# 4.6 Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle. A unit circle has the radius of one it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi using the method explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the in equation x^2+y^2<1.).
pointInsideCircle = 0
NumberOfPoints = int(input("How many random points you want: "))
for i in range(NumberOfPoints):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        pointInsideCircle += 1
piApproximation = 4 * pointInsideCircle / NumberOfPoints
print(f"Approximation of pi using {NumberOfPoints} random points: {piApproximation}")
print("-------------------------------------------------------------------------------------------------")