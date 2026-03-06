# Task: Formatted Output Grading System

while True:
    # 1. Ask for name or 'Exit'
    name_input = input("\nEnter student name (or type 'Exit' to quit): ")

    # 2. Check for the Exit condition
    if name_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    try:
        # 3. Get marks
        mark1 = float(input("Enter mark for subject 1: "))
        mark2 = float(input("Enter mark for subject 2: "))
        mark3 = float(input("Enter mark for subject 3: "))

        # 4. Calculate average and determine grade
        average = (mark1 + mark2 + mark3) / 3
        
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # 5. Formatted Output (Task Requirement) [cite: 105, 123]
        print("\n------------------------------")
        print(f"Name    : {name_input}")
        print(f"Average : {average:.1f}")
        print(f"Grade   : {grade}")
        print("------------------------------")
            
    except ValueError:
        print("Invalid input! Please enter numeric marks.")