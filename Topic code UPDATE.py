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
        input("Do you know what cells are?: ")
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
    print(
        "     Cells are the basic unit of life.They are called the building blocks of us! Basically, they are the reason we exist! We have over thousands of cells around our body, they build tissues, which we will discuss on the next topic.")
    print("")
    print("THREE STATEMENTS OF CELLS")

    print(dialogue["a"])
    print(dialogue["b"])
    print(dialogue["c"])

    print(dialogue["dygi"])
    print(dialogue["E"])
    print(dialogue["N"])


    YesNo = input("Enter: ")

    if YesNo == "e" or YesNo == "E":
        print(dialogue["moveon"])
        break
# TO DO: SHOW NEXT PART

    elif YesNo == "n" or YesNo == "N":
        print(dialogue["uhoh"])


    if YesNo != "e" or YesNo != "E" or YesNo != "n" or YesNo != "N":
        print(dialogue["invalid"])

# TO DO: WHEN THE USER DOESNT PUT A VALID INPUT, DO NOT REPEAT THE LESSON MENTIONED ABOVE.
