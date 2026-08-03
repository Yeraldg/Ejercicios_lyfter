def show_menu():
    print("1. Add student")
    print("2. Show students")
    print("3. Show top 3 students")
    print("4. Export CSV")
    print("5. Import CSV")
    print("6. Exit")

    while True:
            try:
                option = int(input("cuantos videojuegos desea ingresar: "))
                if option <= 0 or option >= 7:
                    print("por favor ingrese un numero positivo (mayor a 0)")
                    continue
                break
            except ValueError:
                print("por favor utilice formato de numero")

    return option