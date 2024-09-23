# Function to get student details and calculate total marks
def get_student_marks():
    name = input("Enter the student's name: ")
    marks = []

    # Input marks for 5 subjects (you can change the number of subjects)
    for i in range(5):
        mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
        marks.append(mark)

    total_marks = sum(marks)
    print(name + "'s total marks: " + str(total_marks))

# Call the function
get_student_marks()
