import csv

def load_file_games(file_path):
    with open(file_path, "r" , encoding='utf-8') as file:
        reader = csv.DictReader(file)
        loaded_games = list(reader)
        return loaded_games

def get_dev():
    dev = input("por favor ingrese la desarrollador, para verificar en nuestra base de datos: ")
    developer = dev.strip().upper()
    return developer

def find_matching_dev(developer, loaded_games):
    games =[]
    for game in loaded_games:
        upper_dev = game["dev"].strip().upper()
        if developer == upper_dev:
            games.append(game)
    return games

def show_games_by_dev (games):
    for game in games:
        print(f"videjuegos desarrollados por: {games[0]['dev']}")
    for game in games:
        print(f" - {game['title']} (Clasificación: {game['classification_esrb']}, Género: {game['genre']})")
        
game_file = load_file_games("videogame_comma.csv")
dev = find_matching_dev("ACTIVISION", game_file)
show_games_by_dev(dev)
        
game_file = load_file_games("videogame_comma.csv")
dev = find_matching_dev("ACTIVISION", game_file)
show_games_by_dev(dev)