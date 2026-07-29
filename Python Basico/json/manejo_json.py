import json

#ejercicio 1
# ya lei el archivo con el link que dice *aqui

#ejercicio 2

def load_json_file(file_path):
    with open(file_path, "r" , encoding='utf-8') as file:
        data = file.read()
        reader = json.loads(data)
        return reader
    
def get_pokemon_basic_info():
    basic_info = {}
    counter = 1
    type_list = []
    
    name = input("por favor ingrese el nombre del pokemon que quieres ingresar a la base de datos: ")
    name = name.strip().capitalize()
    basic_info["name"] = name
    
    while True:
        try:
            type_amount = int(input("cuantos tipos posee este pokemon?: "))
            break
        except ValueError:
            print("por favor ingrese la cantidad de tipos en formato de numero")
            
    while counter <= type_amount:
            pokemon_type = input(f"por favor ingrese el {counter} tipo: ")
            type_list.append(pokemon_type)
            counter += 1
    basic_info["type"] = type_list
        
    while True:
        try:
            level = int(input("que nivel posee este pokemon?: "))
            break
        except ValueError:
            print("por favor ingrese el nivel en formato de numero")
            
    basic_info["level"] = level
    
        
    while True:
        try:
            weight_kg = float(input("que peso en kilogramos posee este pokemon?: "))
            break
        except ValueError:
            print("por favor ingrese el peso en kilogramos en formato de numero")
            
    basic_info["weight_kg"] = weight_kg
        
    return basic_info

def get_pokemon_special_info():
    special_info = {}
    while True:
        is_shiny = input("es un pokemon shiny?(solo se permite si o no): ").strip()
        is_shiny = is_shiny.upper()
        if is_shiny == "SI" or is_shiny == "NO":
            break
        else:
            print("Entrada invalida, por favor intente de nuevo ")
    if is_shiny == "SI":
        special_info["is_shiny"] = True
    else:
        special_info["is_shiny"] = False
    
    while True:
        held_item = input("tiene algun item?(solo se permite si o no): ").strip()
        held_item = held_item.upper()
        if held_item == "SI" or held_item == "NO":
            break
        else:
            print("Entrada invalida, por favor intente de nuevo ")
    if held_item == "SI":
        item_name = input("por favor escriba el nombre de ese item: ").strip()
        special_info["held_item"] = item_name
    else:
        special_info["held_item"] = None
        
    return special_info
        
def get_pokemon_skills():
    pokemon_skills = {}
    skill_list = []
    counter = 1
    while True:
        try:
            skill_amount = int(input("cuantos ataques posee este pokemon?: "))
            break
        except ValueError:
            print("por favor ingrese la cantidad de ataques en formato de numero")
            
    while counter <= skill_amount:
            pokemon_skill = input(f"por favor ingrese el {counter} ataque: ")
            skill_list.append(pokemon_skill)
            counter += 1
            
    pokemon_skills["skills"] = skill_list
    return pokemon_skills
            
def get_pokemon_stats():
    statistics = {}
    stats = {}
    while True:
        try:
            hp = int(input("que hp tiene?: "))
            stats["hp"] = hp
            break
        except ValueError:
            print("por favor utilice formato de numero")
            
    while True:
        try:
            attack = int(input("que nivel de ataque posee este pokemon?: "))
            stats["attack"] = attack
            break
        except ValueError:
            print("por favor utilice formato de numero")
            
    while True:
        try:
            defense = int(input("que nivel de defensa posee este pokemon?: "))
            stats["defense"] = defense
            break
        except ValueError:
            print("por favor utilice formato de numero")
            
    while True:
        try:
            sp_attack = int(input("que velocidad de ataque posee este pokemon?: "))
            stats["sp_attack"] = sp_attack
            break
        except ValueError:
            print("por favor utilice formato de numero")
            
    while True:
        try:
            sp_defense = int(input("que velocidad de defensa posee este pokemon?: "))
            stats["sp_defense"] = sp_defense
            break
        except ValueError:
            print("por favor utilice formato de numero")
            
    while True:
        try:
            speed = int(input("que velocidad general posee este pokemon?: "))
            stats["speed"] = speed
            break
        except ValueError:
            print("por favor utilice formato de numero")
            
    statistics["stats"] = stats
    return statistics

def write_json_file(data_list, new_pokemon, file_path):
    with open(file_path, "w" , encoding='utf-8') as file:
        data_list.append(new_pokemon)
        json.dump(data_list, file, indent=4, ensure_ascii=False)
        
def main():
    file_path = "pokemon.json"
    data_list = load_json_file(file_path)
    new_pokemon = {}
    basic_info = get_pokemon_basic_info()
    special_info = get_pokemon_special_info()
    skills = get_pokemon_skills()
    stats= get_pokemon_stats()
    new_pokemon.update(basic_info)
    new_pokemon.update(special_info)
    new_pokemon.update(skills)
    new_pokemon.update(stats)
    write_json_file(data_list, new_pokemon, file_path)
    
main()
