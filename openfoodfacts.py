#! /usr/bin/env python3
# coding: utf-8

"""
    Docstring
"""

import json
import requests  #pylint: disable=E0401

def main():
    """
        Main function of the script
    """

    #List of the differents categories from openfoodfacts API
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

    #URL https://fr.openfoodfacts.org/categorie/pizza.json
    print("\nTest the connexions with the differents URL...")# pylint: disable=C0325
    print("url = https://fr.openfoodfacts.org/categorie/[category_element].json")# pylint: disable=C0325
    print("-----------------------------------------------------------------------")# pylint: disable=C0325

    for element in category_list:
        quiery_file = requests.get("https://fr.openfoodfacts.org/categorie/{a}.json".format(a=element))# pylint: disable=C0301

        if quiery_file.status_code == requests.codes.ok:
            print("[code: 200] - the category {a} answer well".format(a=element))#pylint: disable=C0325
        else:
            print(quiery_file)#pylint: disable=C0325

    print("-----------------------------------------------------------------------")#pylint: disable=C0325

    #Transfer data into a dictionnary
    dict_element = json.loads(quiery_file.text)
    #Keys of the dictionnary: skip, page_size, products, count, page

    for product in dict_element['products']:
        print(product)#pylint: disable=C0325

    #Check type of the object need to be dict
    print(type(dict_element))#pylint: disable=C0325

if __name__ == "__main__":
    main()
