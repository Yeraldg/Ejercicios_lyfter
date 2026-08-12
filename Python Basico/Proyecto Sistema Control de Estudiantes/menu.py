def show_menu():
    print("1. Add student")
    print("2. Show students")
    print("3. Show top 3 students")
    print("4. Export CSV")
    print("5. Import CSV")
    print("6. Delete Student")
    print("7. View failed student grades")
    print("8. Exit")


    while True:
            try:
                option = int(input("Please choose an option: "))
                if option <= 0 or option >= 9:
                    print("Please enter an option between 1 and 8")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")

    return option