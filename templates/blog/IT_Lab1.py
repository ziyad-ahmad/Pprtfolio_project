# # char = input("Enter a single character: ").lower()
# # if len(char) != 1 or not char.isalpha():
# #     print("Invalid input. Please enter a single alphabet character.")
# # elif char in 'aeiou':
# #     print(f"{char} is a Vowel.")
# # else:
# #     print(f"{char} is a Consonant.")

# Programming Tasks:
# 1.	Even or Odd Number Checker:
# Write a program that asks the user to enter an integer and then prints whether the number is even or odd.
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
#Grade Calculator:
# Create a program that prompts the user to input their name and department. If the department is "IT", ask for their score, And also Based on the score, print their grade according to the following scale:
# 	A: 90–100                          B: 80–89
# 	C: 70–79                            D: 60–69
# 	F: 0–59
full_name = input("Enter your full name: ")
department = input("Enter your department: ").lower()
if department == "it": 
    score = float(input("Enter your score: "))
    if 90 <= score <= 100:
        grade = 'A'
        print(full_name, " your department :", department, "your grade is", grade)
    elif 80 <= score < 90:
        grade = 'B'
        print(full_name, " your department :", department, "your grade is", grade)
    elif 70 <= score < 80:
        grade = 'C'
        print(full_name, " your department :", department, "your grade is", grade)
    elif 60 <= score < 70:
        grade = 'D'
        print(full_name, " your department :", department, "your grade is", grade)
    elif 0 <= score < 60:
        grade = 'F'
        print(full_name, " your department :", department, "your grade is", grade)
    else:
        print("Invalid score. Please enter a score between 0 and 100.")
else:
    print("You are not in the IT department.")
# 2.	Temperature Converter:
# Write a program that asks the user to enter a temperature in Fahrenheit.
# o	Convert it to Celsius, Based on the Celsius temperature, print whether it is:
# 	Freezing (< 0°C)
# 	Normal (0–25°C)
# 	Warm (26–35°C)
# 	Hot (> 35°C)
farnite = float(input("Enter temperature in Fahrenheit: "))
celsius = (farnite - 32) * 5 / 9
if celsius < 0:
    print(celsius,"°C is Freezing.")
elif 0 <= celsius <= 25:
    print(celsius, "°C is Normal.")
elif 26 <= celsius <= 35:
    print(celsius, "°C is Warm.")
elif celsius > 35:
    print(celsius, "°C is Hot.")
# 3.	Vowel or Consonant Checker:
# Create a program that takes a single character input from the user and determines whether it is a vowel or a consonant.
# 4.	BMI Calculator:
# Write a program that calculates a user's Body Mass Index (BMI) based on their height and weight.
# o	Then print their BMI category:
# 	Underweight (< 18.5)
# 	Normal weight (18.5–24.9)
# 	Overweight (25–29.9)
# 	Obese (≥ 30)

