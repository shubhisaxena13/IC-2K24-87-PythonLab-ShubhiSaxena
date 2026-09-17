last_marks = None
last_average = None
last_grade = None


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def enter_student():
    global last_marks, last_average, last_grade

    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = sum(marks) / 5
    grade = calculate_grade(average)

    last_marks = marks
    last_average = average
    last_grade = grade

    print("\nStudent data saved successfully.")


def view_student():
    if last_marks is None:
        print("No student data available.")
    else:
        print("\n----- STUDENT DETAILS -----")
        print("Marks:", last_marks)
        print("Average:", round(last_average, 2))
        print("Grade:", last_grade)


def main():
    while True:
        print("\n----- GRADE CALCULATOR -----")
        print("1. Enter marks for a new student")
        print("2. View grade of last entered student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            print("Exiting Grade Calculator...")
            return

        else:
            print("Invalid choice!")


main()
