#imports
import json
import sleep

#variables
topics_dict = {"a":"cells",
        "b":"tissue",
        "c":"organs",
        "d": "organisms",
        "e":  "eukaryotes",
        "f" :  "prokaryotes"}


#functions
def print_menu_choices(topics):
    for key, value in topics.items():
        print(f"{key}: {value}")
def topics():
    print("placeholder")
def challenges():
    print("placeholder")
def acheivments():
    print("placeholder")
def developers():
    print("placeholder")
#main
while True:
    print_menu_choices(topics_dict)
    choice = input()
    topics()
    challenges()
    acheivments()
    developers()
