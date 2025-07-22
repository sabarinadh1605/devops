try:
    score = int(input("Enter the score: "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"The grade for a score of {score} is: {grade}")

except ValueError:
    print("Invalid input. Please enter a number.")
