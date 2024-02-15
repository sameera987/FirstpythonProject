# Write a program that calculates and displays  the letter grade for a
# given numerical score (e.g A, B, C, D or F)
# based on the following grading scale
# input - score  - 89
# output - B
# A: 90 -100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: 0 -59
# If, elif, else

# Step 1:
# Figure out the inputs
score = int(input("Enter the score: \n"))
# step 2 and step 3:
# Logic
# print A --> if scale >=90 and <=100
# print the output

if score >= 90 and score <= 100:
    print(f"Grade A ")
elif score >= 80 and score <= 89:
    print(f"Grade B ")
elif score >= 70 and score <= 79:
    print(f"Grade C ")
elif score >= 60 and score <= 69:
    print(f"Grade D ")
else:
    print(f"Grade F ")


