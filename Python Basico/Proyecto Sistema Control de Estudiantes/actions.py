
def get_student_name():
    while True:
        number_found = False
        full_name = input("please enter Full Name: ").strip()
        if not full_name:
            print("Please enter a name")
            continue
        for letter in full_name:
            if letter.isdigit():
                number_found = True
        if number_found:
            print("please make sure full name does not include numbers")
            continue
        break
    return full_name
                
def get_student_grade_section():
    while True:
        grade_section = input("please enter grade next to section(e.g. 11B): ").strip().upper()
        if len(grade_section) < 2 or len(grade_section) >= 4:
            print("please make sure to use proper grade/section format")
            continue
        grade = grade_section[:-1]
        section = grade_section[-1]
        if not grade.isdigit() or not section.isalpha():
            print("please make sure to enter grade followed by section")
            continue
        break
    return grade_section

def get_student_spanish_grade():
    while True:
        try:
            spanish_grade = int(input("Please enter Spanish grade: "))
            if spanish_grade < 0 or spanish_grade > 100:
                print("please make sure to enter a grade between 0 and 100")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    return spanish_grade

def get_student_english_grade():
    while True:
        try:
            english_grade = int(input("Please enter English grade: "))
            if english_grade < 0 or english_grade > 100:
                print("please make sure to enter a grade between 0 and 100")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    return english_grade

def get_student_social_studies_grade():
    while True:
        try:
            social_studies_grade = int(input("Please enter Social Studies grade: "))
            if social_studies_grade < 0 or social_studies_grade > 100:
                print("please make sure to enter a grade between 0 and 100")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    return social_studies_grade

def get_student_science_grade():
    while True:
        try:
            science_grade = int(input("Please enter Science grade: "))
            if science_grade < 0 or science_grade > 100:
                print("please make sure to enter a grade between 0 and 100")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    return science_grade

def create_student(students):
    name, section = get_student_info()
    if student_exists(students, name,section):
        print("student already exist.")
        return None
    else:
        student = {
            "full_name" : name,
            "grade_section" : section,
            "spanish_grade" : get_student_spanish_grade(),
            "english_grade" : get_student_english_grade(),
            "social_studies_grade" : get_student_social_studies_grade(),
            "science_grade" : get_student_science_grade()
        }
    return student

def show_csv(students):
    if not students:
        print("There are no records created yet.")
        return
    for student in students:
        print(student)
        
def calculate_students_average(students):
    averages = []
    for student in students:
        name = student["full_name"]
        spanish = int(student["spanish_grade"])
        english = int(student["english_grade"])
        social_studies = int(student["social_studies_grade"])
        science = int(student["science_grade"])
        student_average = (spanish + english + social_studies + science) / 4
        student_info = {
            "name" : name,
            "average" : student_average
        }
        averages.append(student_info)
    
    return averages

def calculate_general_average(averages):
    total = 0
    
    for student in averages:
        total += student["average"]
    general_average = total / len(averages)
    print (f"General average: {general_average}")

def top_3(averages):
    top_students = sorted(
    averages,
    key=lambda student: student["average"],
    reverse=True
    )
    top_3 = top_students[:3]
    position = 1
    for student in top_3:
        print(f"{position}. {student['name']} - average: {student['average']}")
        position += 1
        
def get_student_info():
    name = get_student_name()
    section = get_student_grade_section()
    
    return name, section
    
def student_exists(students, name, section):
    found_student = None
    for student in students:
        if student["full_name"] == name and student["grade_section"] == section:
            print(f"student found: {name}, {section}")
            found_student = student
            break
    if found_student is None:
        print("student not found.")
            
    return found_student

def get_delete_confirmation():
        while True:
            answer = input("would you like to delete the student info(only yes/no): ").strip().upper()
            if answer not in ("YES", "NO"):
                print("please only yes/no answer")
                continue
            break
                
        return answer
    
def delete_student(found_student, students):
    students.remove(found_student)
        
    print("student removed succesfully.")
    
    
def convert_student_info(students):
    all_students = []
    for student in students:
        name = student["full_name"]
        section = student["grade_section"]
        spanish = int(student["spanish_grade"])
        english = int(student["english_grade"])
        social_studies = int(student["social_studies_grade"])
        science = int(student["science_grade"])
        student_info = {
            "name" : name,
            "section" : section,
            "spanish" : spanish,
            "english" : english,
            "social_studies" : social_studies,
            "science" : science 
        }
        all_students.append(student_info)
    return all_students

def find_failed_grades(all_students):
    student_list = []
    for student in all_students:
        failed_grades = {}
        if student["spanish"] < 60:
            failed_grades["spanish"] = student["spanish"]
        if student["english"] < 60:
            failed_grades["english"] = student["english"]
        if student["social_studies"] < 60:
            failed_grades["social_studies"] = student["social_studies"]
        if student["science"] < 60:
            failed_grades["science"] = student["science"]
        if failed_grades:
            student = {
                "name" : student["name"],
                "section" : student["section"],
                "failed_grades" : failed_grades
            }
            student_list.append(student)
        
    return student_list

def show_failed_students(student_list):
    if not student_list:
        print("no students with failed grades")
        return
    for student in student_list:
        name = student["name"]
        section = student["section"]
        print(f"Name: {name}")
        print(f"Section: {section}")
        for subject, grade in student["failed_grades"].items():
            print(f"{subject}: {grade}")
        print("-----------")
    