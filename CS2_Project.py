#imports
import json

#variables
#functions
def print_menu_choices():
    filename = "topics.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        while True:
            choice = input("Input: ")
            print(choice)
            for x in data:
                if x["dict"] == "topics":
                    if choice in x["list"]:
                        z = True
                    else:
                        z = False
            if z == True:
                break
                return choice
            else:
                print("enter valid input")

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
    choice = print_menu_choices()
    topics()
    challenges()
    acheivments()
    developers()
