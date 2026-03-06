#imports
import json

#variables
#functions
def print_menu_choices():
    filename = "topics.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        while True:
            for x in data:
                if x["dict"] == "topics":
                    print(x["choices"])
            choice = input("Input: ")
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
    print("\ntopics placeholder")
def challenges():
    print("challenges placeholder")
def acheivments():
    print("achievments placeholder")
def developers():
    print("developers placeholder\n")
#main
while True:
    choice = print_menu_choices()
    topics()
    challenges()
    acheivments()
    developers()
