#ejercicio 1

import csv


def get_game_amount():
    while True:
        try:
            vgame_total = int(input("cuantos videojuegos desea ingresar: "))
            if vgame_total <= 0:
                print("por favor ingrese un numero positivo (mayor a 0)")
                continue
            break
        except ValueError:
            print("por favor utilice formato de numero")
    return vgame_total
            
def get_videogame_info(vgame_total):
    counter = 1  
    videogame_list = []
        
    while counter <= vgame_total:
        videogame = {
        "title" : input(f"por favor ingrese el nombre del juego {counter}: "),
        "genre" : input (f"ingrese el genero del juego {counter}: "),
        "dev" : input(f"ingrese el nombre del desarrollador {counter}: "),
        "classification_esrb" : input(f"por favor ingrese la clasificacion ESRB {counter}: "),
        }
        videogame_list.append(videogame)
        counter += 1
    return videogame_list

def save_videogame_csv(file_path, data):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = ["title" , "genre" , "dev" , "classification_esrb"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        

def main():
    amount = get_game_amount()
    game_list = get_videogame_info(amount)
    #nombre el archivo asi para diferenciar el ejercicio 1 y 2
    save_videogame_csv('videogame_comma.csv', game_list)
    
main()

#ejercicio 2( va a tomar en cuenta las funciones del ejercicio uno, lo cual es el proposito de las funciones(ser reutilizables))

def save_videogame_tab(file_path, data):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = ["title" , "genre" , "dev" , "classification_esrb"]
        writer = csv.DictWriter(file, fieldnames=headers , dialect=csv.excel_tab)
        writer.writeheader()
        writer.writerows(data)
        
#se que pude incluirlo en el primer main, pero lo hago separado, solo para separar los ejercicios

def main_tab():
    amount = get_game_amount()
    game_list = get_videogame_info(amount)
    save_videogame_tab('videogame_tab.csv', game_list)
    
main_tab()