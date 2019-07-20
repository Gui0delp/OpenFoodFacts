#! /usr/bin/env python3
# coding: utf-8

"""
    Docstring
"""

import json
import time
import requests  #pylint: disable=E0401


def convert_time(time_convert):
    """
        Function permit to convert time into minutes and seconds
        This function take a float
        Return int (minutes and secondes)
    """
    minutes_t = round(time_convert / 60, 0)
    seconds_t = round(time_convert % 60, 0)

    print("Execution time: {a} m {b} s\n".format(a=int(minutes_t), b=int(seconds_t)))
    #return minutes_t, seconds_t

def main():
    """
        Main function of the script
    """

    time_start = 0
    time_end = 0
    time_result = 0
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

    time_start = time.time()

    for element in category_list:
        quiery_file = requests.get("https://fr.openfoodfacts.org/categorie/{a}.json".format(a=element))# pylint: disable=C0301

        if quiery_file.status_code == requests.codes.ok:
            print("[code: 200] - the category {a} answer well".format(a=element))#pylint: disable=C0325
        else:
            print(quiery_file)#pylint: disable=C0325

    print("-----------------------------------------------------------------------")#pylint: disable=C0325

    time_end = time.time()
    time_result = time_end - time_start
    convert_time(time_result)


    #Transfer data into a dictionnary
    dict_element = json.loads(quiery_file.text)
    #Keys of the dictionnary: skip, page_size, products, count, page

    for key, value in dict_element.items():
        if key == "products":
            list_product = value

    #OK
    #for elements in list_product:
        #print(type(elements))
        #for element in elements:
            #if element == "product_name":
                #print(element)

    for elements in list_product:
        for key, element in elements.items():
            if key == "product_name":
                print(element)


if __name__ == "__main__":
    main()
