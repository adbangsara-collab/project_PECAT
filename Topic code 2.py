import json

filename = "dialogue.json"

with open(filename) as f:
    dialogue = json.load(f)

filename2 = "2nd dialog.json"
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
    print(dialogue2["Introtiss"])
    print(dialogue2["a2"])
    print(dialogue2["b2"])
    print(dialogue2["c2"])

    input()

    print(dialogue2["resptiss"])
    print(dialogue2["start"])
    print(  dialogue2["block"])

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

        print(dialogue2["Ttypes"])
        print(dialogue2["ET"])
        print(  dialogue2["ETex1"])
        print(  dialogue2["ETex2"])

        print(dialogue2["CT"])
        print(  dialogue2["CTex1"])
        print(  dialogue2["CTex2"])

        print(dialogue2["MT"])
        print(  dialogue2["MTex1"])
        print(  dialogue2["MTex2"])
        print(      dialogue2["MTex3"])
        print(      dialogue2["MTex4"])
        print(      dialogue2["MTex5"])

        print(dialogue2["CT"])
        print(dialogue2["NTex1"])
        print(dialogue2["NTex2"])

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