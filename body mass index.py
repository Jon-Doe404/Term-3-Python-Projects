# Jon Joseph Catipon
# The user chooses between metric (kg/m) or imperial (lbs/in) by entering 1 or 2.
# Then, the program asks for weight and height.
# It calculates BMI using the correct formula based on the chosen unit.
# 4/4/2025
# 2024-140029

print("Body Mass Index (BMI) Calculator")  

print("\nChoose your unit system:")
print("1 - Metric (kg/m)")
print("2 - Imperial (lbs/in)")
choice = input("Enter 1 or 2: ").strip()

if choice == "2":
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = (weight / (height * height)) * 703

elif choice == "1":
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height * height)

else:
    print("Invalid choice. Please restart and enter 1 or 2.")
    exit()

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
