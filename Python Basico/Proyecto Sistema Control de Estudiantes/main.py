from data import create_csv, read_csv

def main():
    students = []
    file_path =  "student_database.csv"
    create_csv(file_path, students)
    read_csv(file_path)
    
main()