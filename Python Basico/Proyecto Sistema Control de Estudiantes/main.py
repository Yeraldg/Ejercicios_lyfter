from data import create_csv, read_csv
from menu import show_menu
from actions import create_student

def main():
    file_path =  "student_database.csv"
    students = []
    while True:
        option = show_menu()
        if option == 1:
            student = create_student()
            students.append(student)
    
main()