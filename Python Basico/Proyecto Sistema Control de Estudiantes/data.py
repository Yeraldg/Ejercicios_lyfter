import csv

def create_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = ["first_name" , "grade_section" , "spanish_grade" , "english_grade" , "social_studies_grade" , "science_grade"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        
def read_csv(file_path):
    with open(file_path, "r" , encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for line in reader:
            for header, value in zip(headers, line):
                return(f"{header}: {value}")
            
            