# Jon Joseph Catipon
# This program takes a list of numbers from the user until they enter a blank line.
# It then separates them into negatives, zeros, and positives.
# The numbers are printed in the same order they were entered, grouped accordingly.
# 4/4/2025
# 2024-140029

values = []
while True:
    line = input("Enter a number (blank to enter): ")
    if line == "":
        break
    try:
        num = int(line)
    except:
        print("Please enter a valid integer.")
        continue
    values.append(num)

neg = []
zero = []
pos = []

for v in values:
    if v < 0:
        neg.append(v)
    elif v == 0:
        zero.append(v)
    else:
        pos.append(v)

for n in neg + zero + pos:
    print(n)
