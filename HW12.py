import json
from pprint import pp

chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36}
]



def create_file(path,fileName):
    try:
        with open(f"{path}/{fileName}",mode='x',encoding="utf-8"):
            pass
    except FileExistsError:
        pass


def read_file(path):
    try:
        with open(path,mode='r',encoding='utf-8') as file:
            return json.loads(file.read())
    except json.decoder.JSONDecodeError as err:
        print('')


def write_in_file(path,text):
    with open(path,mode='w',encoding='utf-8') as file:
        text.sort(key=lambda x:x['id'])
        file.write(json.dumps(text,indent=2))


def update_file(path,text):
    
    data = read_file(path)
    temp = str(data)
    for i in text:
        if f"'id': {i['id']}" not in temp:
            data += [i]
        
    data.sort(key=lambda x: x['id'])
    with open(path,mode='w',encoding='utf-8') as file:
        file.write(json.dumps(data,indent=2))


