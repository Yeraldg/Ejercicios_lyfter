
def get_student_info():
    while True:
        number_found = False
        first_name = input("please enter Full Name: ")
        first_name.split
        for letter in first_name:
            if letter.isdigit():
                number_found = True
        if number_found:
            print("please make sure full name does not incude numbers")
            continue
        else:
            break
    return first_name
                
