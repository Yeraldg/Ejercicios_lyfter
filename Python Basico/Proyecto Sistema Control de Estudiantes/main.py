from data import create_csv, read_csv
from menu import show_menu
from actions import create_student, show_csv, calculate_students_average, calculate_general_average, top_3, get_delete_confirmation, student_exists, delete_student, get_student_info, convert_student_info,find_failed_grades, show_failed_students

def main():
    file_path =  "student_database.csv"
    students = read_csv(file_path)
    while True:
        option = show_menu()
        if option == 1:
            student = create_student(students)
            if student:
                students.append(students)
                create_csv(file_path, students)
                print("Student added")
        elif option == 2:
            print("students on record: ")
            show_csv(students)
        elif option == 3:
            averages = calculate_students_average(students)
            calculate_general_average(averages)
        elif option == 4:
            averages = calculate_students_average(students)
            print("the top 3 students are: ")
            top_3(averages)
        elif option == 5: 
            create_csv("students_export.csv", students)
            print("Students exported successfully.")
        elif option == 6:
            students = read_csv("students_export.csv")
            if students:
                print("Students imported successfully.")
            else:
                print("There is no exported file to import.")
        elif option == 7:
            name, section = get_student_info()
            student_to_delete = student_exists(students, name, section)
            if student_to_delete:
                answer  = get_delete_confirmation()
                if answer == "YES":
                    delete_student(student_to_delete, students)
                    create_csv(file_path,students)
        elif option == 8:
            all_students = convert_student_info(students)
            student_list = find_failed_grades(all_students)
            show_failed_students(student_list)
        elif option == 9:
            print("menu closed")
            break
    
main()