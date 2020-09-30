#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        values = [input("Entrer une valeur")for _ in range(10)]
    return values == sorted(values)
    
def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        words = [sorted(input("entez un mot ")), sorted(input("entrez un autre mot "))]
        
    if words[0] == words[1]:
        print("ce sont des annagrammes") 
    else:
        print("ce ne sont pas des annagrammes") 


def contains_doubles(items: list) -> bool:
    my_list = [3, 3, 5, 6, 1, 1]
    uniques = set(my_list)
    return len(uniques) == len(my_list)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    list_student, list_grades = [], []
    nom, note = None, None
    for student in student_grades:
        student_grades[student] = sum(student_grades[student]) / len(student_grades[student])
        list_student.append(student)
        list_grades.append(student_grades[student])
        
    for student in range(len(list_student)):
        if list_grades[student] > list_grades[student-1]:
            nom = list_student[student]
            note = list_grades[student]
            return nom, note
    


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres
    histohramme = {}
    for char in sentence:
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
    frequency = 5
    most_frequent_chars = [k for k, v in histogram.items() if v > frequency and key != " "]
    
   
    return hist, most_frequent_chars


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    recipe = input("Veuilles entrer le nom d'une recette. ")
    nb_ingredients = int(input("veuiller entrer le nombre d'ingrédients. "))
    ingredients = tuple(input("Veuiller entrer un ingrédient. ")for i in range(nb_ingredients))
    recipe_book = {recipe: ingredients}



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    desired_recipe = input("Veuillez entrez la recette désiré. ")
   return 

def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
