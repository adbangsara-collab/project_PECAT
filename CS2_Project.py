#imports
import json

#variables

#functions
def instructs(): # prints instructions

    filename = "instructions.json" # open file
    with open(filename, 'r') as file:
        instructions = json.load(file)

        print("="*20)
        print(instructions["I"])
        print(instructions["Dl"])
        print(instructions["1L"])
        print("~" * 20)
        print(instructions["2L"])
        print("~" * 20)
        print(instructions["3L"])
        print("~" * 20)
        print(instructions["4L"])
        print("~" * 20)

        print(instructions["Q"])
        print(instructions["1Q"])
        print("~" * 20)
        print(instructions["2Q"])
        print("~" * 20)
        print(instructions["3Q"])
        print("~" * 20)
        print(instructions["4Q"])
        print("~" * 20)
        print("=" * 20)

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
                        break
                    else:
                        print("enter valid input")
            print(x["choices2"])
            while True:# loops until valid input
                        choice2 = input("Input: ")
                        if choice2 in x["list2"]:
                            break
                        else:
                            print("enter valid input")
            for x in data:
                if x["dict"] == choice1:
                    print(x[str(choice2)]) # we will make this display text, video or graphic in the future when th files are good


def challenges(): # function for challenges option
    if choice == "b":
        filename = "challenges.json"
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            x = data
            print(x["choices1"])
            while True:  # loops until valid input
                choice1 = input("Input: ")
                if choice1 in x["list1"]:
                    break
                else:
                    print("enter valid input")
            file.close()
        filename = f"challenges_{choice1}.json"
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            x = data
            dialog1 = x["dialog1"]
            correct = 0
            for z in range(1, 6):
                tries = 0
                while True:
                    answers1 = x["answers1"]
                    print(dialog1[str(z)])
                    tries += 1
                    while True:  # loops until valid input
                        answer = input("Input: ")
                        if answer in x["valid_ans1"]:
                            break
                        else:
                            print("Enter valid input: ")
                    if answer.lower() == answers1[(z-1)]:
                        dialog_ans1 = x["dialog_ans1"]
                        print(dialog_ans1["correct"])
                        correct += 1
                        break
                    elif tries == 1:
                        dialog_ans1 = x["dialog_ans1"]
                        print(dialog_ans1["incorrect1"])
                    else:
                        dialog_ans1 = x["dialog_ans1"]
                        print(dialog_ans1["incorrect2"])
                        break
            dialog2 = x["dialog2"]
            for z in range(1, 6):
                while True:
                        answers2 = x["answers2"]
                        print(dialog2[str(z)])
                        while True:  # loops until valid input
                            answer = input("Input: ")
                            if answer in x["valid_ans2"]:
                                break
                            else:
                                print("enter valid input")
                        if answer.lower() == answers2[(z-1)]:
                            dialog_ans2 = x["dialog_ans2"]
                            print(dialog_ans2["correct"])
                            break
                        else:
                            dialog_ans2 = x["dialog_ans2"]
                            print(dialog_ans2["incorrect"])
                        break
            if correct == 6:
                print(x["pass"])
            else:
                print(x["fail"])
            print(f"You got {correct} correct out of 10")
        filename = f"acheivments.json"
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if correct == 6:
                data[choice1] = "solved"
                json.dump(data, file)


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
