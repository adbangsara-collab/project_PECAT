print("Hello user!")
print("Can I ask you  a question?")

print("[Press e if yes]")
print("[Press n if no]")

YesNo = input("Enter: ")


if YesNo == "e" or YesNo == "E":
    input("Do you know what cells are?: ")
    print("Great! Because this is what we are gonna talk about today!")
    
elif YesNo == "n" or YesNo == "N":
    print("We’re gonna discuss it anyway.")
    
else: print("Give me a valid input. >:[.")

# Theres supposed to be a function here where the program will loop unless user gives a proper input
    
print("Content:")
print("     Cells are the basic unit of life.They are called the building blocks of us! Basically, they are the reason we exist! We have over thousands of cells around our body, they build tissues, which we will discuss on the next topic.")
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
# TO DO: SHOW NEXT PART
    
elif YesNo == "n" or YesNo == "N":
    print("Read it again for further information.")
    
# TO DO: LOOP THIS PART UNTIL USER'S INPUT IS "e" OR "E"
    
else: print("Give me a valid input. >:[.")

# Again, theres supposed to be a function here where the program will loop unless user gives a proper input


