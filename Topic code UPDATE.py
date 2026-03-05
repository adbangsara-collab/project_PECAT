print("Hello user!")
print("Can I ask you  a question?")

print("[Press e if yes]")
print("[Press n if no]")

cont = False
while cont == False:
    YesNo = input("Enter: ")

    if YesNo == "e" or YesNo == "E":
        input("Do you know what cells are?: ")
        print("Great! Because this is what we are gonna talk about today!")

        break

    elif YesNo == "n" or YesNo == "N":
        print("We’re gonna discuss it anyway.")

        break


    else:
        print("Give me a valid input. >:[.")


cont = False
while cont == False:
    print("Content:")
    print(
        "     Cells are the basic unit of life.They are called the building blocks of us! Basically, they are the reason we exist! We have over thousands of cells around our body, they build tissues, which we will discuss on the next topic.")
    print("")
    print("THREE STATEMENTS OF CELLS")

    print("A) Every living thing are made of cells")
    print("B) Cells are the basic unit of life")
    print("C) Cells come from pre existing cells")

    print("Do you get it?")
    print("[Press e if yes]")
    print("[Press n if no]")


    YesNo = input("Enter: ")

    if YesNo == "e" or YesNo == "E":
        print("Great! We can now move on to the next part!")
        break
# TO DO: SHOW NEXT PART

    elif YesNo == "n" or YesNo == "N":
        print("Read it again for further information.")


    if YesNo != "e" or YesNo != "E" or YesNo != "n" or YesNo != "N":
        print("Give me a valid input. >:[.")

# TO DO: WHEN THE USER DOESNT PUT A VALID INPUT, DO NOT REPEAT THE LESSON MENTIONED ABOVE.
print("TYPE OF CELLS inside our body")
print("	Red blood cells")
print("Also called erythrocyte")
print(" Cells that transport oxygen to the lungs and release carbon dioxide from the lungs.")
print("Without erythrocytes, we cannot function the respiratory system and lead to your sad death.")

print("	White blood cells")
print(" Also called leukocytes")
print(" Fights infections and diseases to protect your human body.")
print("Without leukocytes, we could get sick easily and eventually and probably would lead to a sad death.")

print("Do you get it?")
print("		[Press e if yes]")
print("		[Press n if no]")
YesNo = input("Enter: ")

cont = False
while cont == False:
    if YesNo == "e" or YesNo == "E":
        print("Great! We can now move on to the next part. The quiz!")
        break
# TO DO: GO STRAIGHT TO THE QUIZ

    elif YesNo == "n" or YesNo == "N":
        print("Read it again for further information.")


        if YesNo != "e" or YesNo != "E" or YesNo != "n" or YesNo != "N":
            print("Give me a valid input. >:[.")






