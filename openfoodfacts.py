#! /usr/bin/env python3
# coding: utf-8

"""
    Docstring
"""

import json
import requests

def main():
    """
        Main function of the script
    """

    req_url = ''

    #Je liste les catégories à recupérer category_list
    #Je boucle sur la liste

    #List of the different categories#List of the different categories from openfoodfacts API
    category_list = [\
        "conserves",\
        "pizzas",\
        "plats",\
        "yaourts",\
        "jambons",\
        "barres-de-cereales",\
        "sauces",\
        "pates-alimentaires",\
        "biscuits",\
        "legumes-et-derives"]

    response = requests.get('https://fr.openfoodfacts.org/categorie/pizza.json')
    print(response)

if __name__ == "__main__":
    main()
