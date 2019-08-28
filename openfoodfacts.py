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

    print("Execution time: {a} m {b} s".format(a=int(minutes_t), b=int(seconds_t)))#pylint: disable=C0325
    #return minutes_t, seconds_t

def main():
    """
        Main function of the script
    """

    time_start = 0
    time_end = 0
    time_result = 0
    name = ""
    code = ""
    nutri_gr_fr = ""
    url_items = ""
    store = ""
    origins_items = ""
    list_category = []
    #List of the differents categories from openfoodfacts API
    category_list = [\
        "conserves",\
        "plats",\
        "legumes-et-derives",\
        "yaourts",\
        "jambons",\
        "barres-de-cereales",\
        "sauces",\
        "pates-alimentaires",\
        "biscuits",\
        "pizzas"]

    #URL https://fr.openfoodfacts.org/categorie/pizza.json
    print("\nTest the connexions with the differents URL...")# pylint: disable=C0325
    print("url = https://fr.openfoodfacts.org/categorie/[category_element].json")# pylint: disable=C0325
    print("-----------------------------------------------------------------------")# pylint: disable=C0325

    time_start = time.time()

    for element in category_list:
        quiery_file = requests.get("https://fr.openfoodfacts.org/categorie/{a}.json".format(a=element))# pylint: disable=C0301

        if quiery_file.status_code == requests.codes.ok:
            print("[code: 200] - the category {a} answer well".format(a=element))#pylint: disable=C0325
            #Transfer data into a dictionnary
            dict_element = json.loads(quiery_file.text)

            #Keys of the dictionnary: skip, page_size, products, count, page
            for key, value in dict_element.items():
                if key == "products":
                    list_category.append(value)
                else:
                    pass

    print("-----------------------------------------------------------------------")#pylint: disable=C0325

    time_end = time.time()
    time_result = time_end - time_start
    convert_time(time_result)
    print("-----------------------------------------------------------------------")#pylint: disable=C0325

    #This loop search the key product name and print the value

    i = 0
    for category in category_list:
        index_product = 0
        for key, value in list_category[i][index_product].items():
            if key == "product_name":
                name = value
            elif key == "code":
                code = value
            elif key == "nutrition_grade_fr":
                nutri_gr_fr = value
            elif key == "url":
                url_items = value
            elif key == "stores":
                store = value
            elif key == "labels":
                origins_items = value
            else:
                pass
        i += 1
        index_product += 1

        print("{a} | name: {b} | code: {c} | nutri score: {d} | store: {f} | origine: {g}| url: {e}" \
        .format(\
         a=index_product,\
         b=name,\
         c=code,\
         d=nutri_gr_fr,\
         e=url_items,\
         f=store,\
         g=origins_items,\
         ))#pylint: disable=C0325

    print("-----------------------------------------------------------------------\n")#pylint: disable=C0325

if __name__ == "__main__":
    main()
