from data import create_csv, read_csv
from menu import show_menu
from actions import create_student, show_csv, calculate_students_average, top_3, get_delete_confirmation, student_exists, delete_student, get_student_info

def main():
    file_path =  "student_database.csv"
    students = read_csv(file_path)
    while True:
        option = show_menu()
        if option == 1:
            student = create_student()
            students.append(student)
            create_csv(file_path, students)
            print("Student added")
        elif option == 2:
            print("students on record: ")
            show_csv(file_path)
        elif option == 3:
            print("the top 3 students are: ")
            averages = calculate_students_average(file_path)
            top_3(averages)
        elif option == 4: 
            create_csv("students_export.csv", students)
            print("Students exported successfully.")
        elif option == 5:
            students = read_csv("students_export.csv")
            if students:
                print("Students imported successfully.")
            else:
                print("There is no exported file to import.")
        elif option == 6:
            name, section = get_student_info()
            student_to_delete = student_exists(students, name, section)
            if student_to_delete:
                answer  = get_delete_confirmation()
                if answer == "YES":
                    delete_student(student_to_delete, students)
                    create_csv(file_path,students)
    
main()