
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

def create_student():
    student = {
        "name" : get_student_name(),
        "grade_section" : get_student_grade_section(),
        "spanish_grade" : get_student_spanish_grade(),
        "english_grade" : get_student_english_grade(),
        "social_studies_grade" : get_student_social_studies_grade(),
        "science_grade" : get_student_science_grade()
    }
    return student