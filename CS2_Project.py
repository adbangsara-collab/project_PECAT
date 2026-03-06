#imports
import json

#variables
#functions
def instructs():

    import json

    filename = "instructions.json"
    with open(filename, 'r') as file:
        instructions = json.load(file)

        print(instructions["I"])
        print(instructions["Dl"])
        print(instructions["1L"])
        print(instructions["2L"])
        print(instructions["3L"])
        print(instructions["4L"])

        print(instructions["Q"])
        print(instructions["1Q"])
        print(instructions["2Q"])
        print(instructions["3Q"])
        print(instructions["4Q"])

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
    instructs()
    choice = print_menu_choices()
    topics()
    challenges()
    acheivments()
    developers()
