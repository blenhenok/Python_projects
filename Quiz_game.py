print("Welocome to my quiz game")

playing = input ("do you want to play this game: ")
if playing != "yes":
    quit()
print("let's go :) ")

score = 0

quiz = input ("what is my full name? ")
if quiz.capitalize() == "blen henok":
    print("correct!")
    score += 1
elif quiz.capitalize() == "blen":
    print ("everyone knows that. i asked my full name.")
else:
    print("you do not even know my full name!")
    missed= input ("do you even wanna continue after this? ")
    if missed.lower() == "yes":
        print("do not have hope but let's continue!")
    else:
        quit()

quiz = input("who is my celebrity crush? ")
if quiz.capitalize() == "kim min kyu":
    print("correct!")
    score += 1
else:
    print("Nope :( ")

quiz = input("what is my favorite animal? ")
if quiz.upper() == "all":
    print("correct!")
    score += 1
else:
    print("there is no such thing as favorite animal. i love them all! ")

quiz = input("what is my favorite place in the world? ")
if quiz == "my room":
    print("correct!")
    score += 1
else:
    print("Nope :( ")

quiz = input("what is my favorite genre of music? ")
if quiz.upper() == "hip hop":
    print("correct!")
    score += 1
else:
    print("Nope :( ")

quiz = input("what is my favorite possession? ")
if quiz == "pc":
    print("correct!")
    score += 1
elif quiz == "laptop":
    print("correct!")
    score += 1
else:
    print("Nope :( ")

quiz = input("tea or coffee? ")
if quiz == "coffee":
    print("correct!")
    score += 1
else:
    print("Nope :( ")

quiz = input("chocolate or ice cream? ")
if quiz == "ice cream":
    print("correct!")
    score += 1
else:
    print("Nope :( ")

quiz = input("going out or staying in? ")
if quiz == "staying in":
    print("correct!")
    score += 1
else:
    print("Nope :( ")

quiz = input("who is my favorite music artist? ")
if quiz.upper() == "NF":
    print("correct!")
    score += 1
else:
    print("Nope :( ")


print("you answered " + str(score) + " correctly")
if "score" >= "5":
    print("not bad :)")
else:
    print("you do not deserve this chance")
