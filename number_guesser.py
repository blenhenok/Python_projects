import random
# randrange (-1, 10) it doesn't include the upper bound number so it gives [-1, 9]
#randint(-1,10) it includes the upper bound number so it gives [-1,10]

top_range = input("Type a number: ")
if top_range.isdigit():  #since all inputs are strings it will check if the input is a digit
    top_range = int(top_range)  #int will then convert the string input to an integer
    if top_range < 0:
        print("the number should be greater than zero!")
        quit()
else:
    quit()
    

rand_number = random.randint(0, top_range)
guesses = 0
while True:
    guesses += 1 #this keeps track of the number of guesses we can make
    user_guess = input("then a guess number between 0 and " + str(top_range) +": ")
    if user_guess.isdigit():  #since all inputs are strings it will check if the input is a digit
        user_guess = int(user_guess)  #int will then convert the string input to an integer
    else:
        print("write a number next time!")
        continue
    
    if user_guess == rand_number:
        print("you got it correct!")
        break
    elif user_guess > rand_number:
        print("you are guessing above the number , guess a smaller number.")
    else:
        print("you are guessing small number, the number is greater than your previous guess.")

print("you got it in your", guesses, "th try")



