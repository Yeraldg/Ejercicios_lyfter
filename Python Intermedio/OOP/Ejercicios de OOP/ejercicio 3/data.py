import csv
import os
from actions import Student

def student_to_dict(student):
    return {
        "full_name": student.full_name,
        "grade_section": student.grade_section,
        "spanish_grade": student.spanish_grade,
        "english_grade": student.english_grade,
        "social_studies_grade": student.social_studies_grade,
        "science_grade": student.science_grade
    }

def create_csv(file_path, data):
    student_dict = []
    for student in data:
        student_dict.append(student_to_dict(student))
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = ["full_name" , "grade_section" , "spanish_grade" , "english_grade" , "social_studies_grade" , "science_grade"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(student_dict)
        
def read_csv(file_path):
    students = []
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r" , encoding='utf-8') as file:
        csv_reader =csv.DictReader(file)
        for student in csv_reader:
            stored_student = Student(
                student["full_name"],
                student["grade_section"],
                student["spanish_grade"],
                student["english_grade"],
                student["social_studies_grade"],
                student["science_grade"]
                )
            students.append(stored_student)
        
        return students

