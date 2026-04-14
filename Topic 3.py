import json

filename = "dialogue.json"

with open(filename) as f:
    dialogue = json.load(f)

filename2 = "TopicDialogue3.json"

with open(filename2) as f:
    dialogue2 = json.load(f)

print(dialogue["greet"])
print(dialogue["ask"])
print(dialogue["E"])
print(dialogue["N"])

cont = False
while cont == False:
    YesNo = input("Enter: ")

    if YesNo == "e" or YesNo == "E":
        input("Do you know what organs are?: ")
        print(dialogue["praise"])

        break

    elif YesNo == "n" or YesNo == "N":
        print(dialogue["nope"])

        break


    else:
        print(dialogue["invalid"])

cont = False
while cont == False:
    print("Content:")
    print(dialogue2["qhook"])
    print(dialogue2["a3"])
    print(dialogue2["b3"])
    print(dialogue2["c3"])
    print(dialogue2["d3"])

    input()

    print(dialogue2["response"])
    print(dialogue2["begin"])
    print(  dialogue2["organs"])

    print(dialogue["dygi"])
    print(dialogue["E"])
    print(dialogue["N"])

    YesNo = input("Enter: ")

    if YesNo == "e" or YesNo == "E":
        print("Great! We can now move on to the next part!")
        break



    elif YesNo == "n" or YesNo == "N":
        print("Read it again for further information.")


    if YesNo != "e" or YesNo != "E" or YesNo != "n" or YesNo != "N":
        print(dialogue["invalid"])

        print(dialogue2["diff"])
        print(dialogue2["3A"])
        print(  dialogue2["3A2"])
        print(  dialogue2["ExIn"])
        print(  dialogue2["ex"])

        print(dialogue2["B"])
        print(  dialogue2["B2"])

        print(dialogue2["C1"])
        print(dialogue2["C2"])
        print(dialogue2["ex2"])

        print(dialogue2["D1"])
        print(dialogue2["D2"])
        print(dialogue2["ex3"])
        print(dialogue2["D3"])

        print(dialogue["dygi"])
        print(dialogue["E"])
        print(dialogue["N"])

        YesNo = input("Enter: ")

        if YesNo == "e" or YesNo == "E":
            print("Great! We can now move on to the next part!")
            break


        elif YesNo == "n" or YesNo == "N":
            print("Read it again for further information.")

        if YesNo != "e" or YesNo != "E" or YesNo != "n" or YesNo != "N":
            print(dialogue["invalid"])