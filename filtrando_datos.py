from functools import reduce

# Cuando se coloca una variable en mayúscula en realidad se denomina constante, es decir, no se espera cambiar su contenido.
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    # adults = list(map(lambda worker: worker["name"], adults))

    # Para sumar diccionarios se utiliza | que significa pipe.
    # olds = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    
    # Usando High order functions se filtra los nombre de todos los devs que trabajan con Python
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    # Usando High order functions se filtra los nombres de todos los trabajadores que trabajan en Platzi
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))

    # Usando List comprehensions se filtra los nombres de los trabajadores que son mayores de edad
    adult_workers = [worker["name"] for worker in DATA if worker["age"] >= 18]
   
    # Usando List Comprehensions se agrega a los diccionarios la llave OLD que puede tener el valor de True or False
    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]
   
    for worker in old_people:
        print(worker)

        



if __name__ == '__main__':
    run()