student_grades = {
    "Alice": "B",
    "Bob": "C",
    "Charlie": "A"
}

def manage_grades():
    while True:
        print("\n--- Student Grade Menu ---")
        print("1. Add a new student and grade")
        print("2. Update an existing student's grade")
        print("3. Print all student grades")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student's letter grade (e.g., A, B, C): ")
            student_grades[name] = grade.upper()
            print(f"Added {name} with a grade of {student_grades[name]}.")
        elif choice == '2':
            name = input("Enter student name to update: ")
            if name in student_grades:
                grade = input(f"Enter new letter grade for {name}: ")
                student_grades[name] = grade.upper()
                print(f"Updated {name}'s grade to {student_grades[name]}.")
            else:
                print(f"Student '{name}' not found.")
        elif choice == '3':
            print("\n--- All Student Grades ---")
            if not student_grades:
                print("No student grades to display.")
            else:
                for name, grade in student_grades.items():
                    print(f"{name}: {grade}")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

manage_grades()
