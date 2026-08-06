import csv
import os

def create_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = ["full_name" , "grade_section" , "spanish_grade" , "english_grade" , "social_studies_grade" , "science_grade"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        
def read_csv(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r" , encoding='utf-8') as file:
        csv_reader =csv.DictReader(file)
        students = list(csv_reader)
        
        return students

