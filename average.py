# Jon Joseph Catipon
# This program calculates the average of numbers entered by the user.
# The user keeps entering numbers until they enter 0, which stops the input.
# If 0 is the first number entered, an error message is shown.
# 4/4/2025
# 2024-140029

numbers = []
while True:
    val = input("Enter a number (0 to enter): ")
    try:
        num = float(val)
    except:
        print("Invalid input. Please enter a number.")
        continue
    if num == 0:
        break
    numbers.append(num)

if len(numbers) == 0:
    print("You didn't enter any numbers.")
else:
    total = 0
    for n in numbers:
        total += n
    avg = total / len(numbers)
    print("Average:", avg)
