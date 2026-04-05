import json

filename = "dialogue.json"

with open(filename) as f:
    dialogue = json.load(f)

print(dialogue["greet"])
print(dialogue["ask"])
print(dialogue["E"])
print(dialogue["N"])

cont = False
while cont == False:
    YesNo = input("Enter: ")

    if YesNo == "e" or YesNo == "E":
        input("Do you know what tissues are?: ")
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
    print(dialogue["Introtiss"])
    print(dialogue["a2"])
    print(dialogue["b2"])
    print(dialogue["c2"])

    input()

    print(dialogue["resptiss"])
    print(dialogue["start"])
    print(  dialogue["block"])

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

        print(dialogue["Ttypes"])
        print(dialogue["ET"])
        print(  dialogue["ETex1"])
        print(  dialogue["ETex2"])

        print(dialogue["CT"])
        print(  dialogue["CTex1"])
        print(  dialogue["CTex2"])

        print(dialogue["MT"])
        print(  dialogue["MTex1"])
        print(  dialogue["MTex2"])
        print(      dialogue["MTex3"])
        print(      dialogue["MTex4"])
        print(      dialogue["MTex5"])

        print(dialogue["CT"])
        print(dialogue["NTex1"])
        print(dialogue["NTex2"])

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