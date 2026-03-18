#imports
import json

#variables
#functions
def instructs(): # prints instructions

    filename = "instructions.json" # open file
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

def print_menu_choices(): # prints menu and gets choice
    filename = "menu.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        while True:# loops until valid input
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
                return choice
            else:
                print("enter valid input")

def topics(choice): # function for topic option
    if choice == "a":
        filename = "topics.json"
        with open(filename, 'r') as file:
            data = json.load(file)
            x = data[0]
            print(x["choices1"])
            while True: # loops until valid input
                    choice1 = input("Input: ")
                    if choice1 in x["list1"]:
                        z = True
                    else:
                        z = False
                    if z == True:
                        break
                    else:
                        print("enter valid input")
            print(x["choices2"])
            while True:# loops until valid input
                        choice2 = input("Input: ")
                        if choice2 in x["list2"]:
                            z = True
                        else:
                            z = False
                        if z == True:
                            break
                        else:
                            print("enter valid input")
                        break
            for x in data:
                if x["dict"] == choice1:
                    print(x[choice2]) # we will make this display text, video or graphic in the future when th files are good


def challenges(): # function for chyallenges option
        if choice == "b":
            filename = "challenges.json"
            with open(filename, 'r',encoding='utf-8') as file:
                data = json.load(file)
                x = data[0]
                print(x["choices1"])
                while True:  # loops until valid input
                    choice1 = input("Input: ")
                    if choice1 in x["list1"]:
                        z = True
                    else:
                        z = False
                    if z == True:
                        break
                    else:
                        print("enter valid input")
                for x in  data:
                    if x["dict"] == choice1:
                        break
                y = x["dialog1"]
                for z in range(1,5):
                    print(y[str(z)])

def acheivments():# function for acheivment option
    print("achievments placeholder")
def developers():# function for developers option
    print("developers placeholder\n")
#main
while True:
    instructs()
    choice = print_menu_choices()
    topics(choice)
    challenges()
    acheivments()
    developers()
