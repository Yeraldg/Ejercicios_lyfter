def show_menu():
    print("1. Add student")
    print("2. Show students")
    print("3. General average")
    print("4. Show top 3 students")
    print("5. Export CSV")
    print("6. Import CSV")
    print("7. Delete Student")
    print("8. View failed student grades")
    print("9. Exit")


    while True:
            try:
                option = int(input("Please choose an option: "))
                if option <= 0 or option >= 10:
                    print("Please enter an option between 1 and 9")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")

    return option