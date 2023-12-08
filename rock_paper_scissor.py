import random

user_win = 0
cptr_win = 0
option = ["rock", "paper", "scissors"]

while True:
    user_input = input("chose between rock/paper.scissors and Q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input not in option:
        continue

    rand_number = random.randint(0,2)
    # 0=rock, 1=paper, 2=scissors
    cptr_pick = option[rand_number]
    print("computer picks", cptr_pick + ".")

    if user_input == "rock" and cptr_pick == "scissors":
        print("you won!")
        user_win += 1
    if user_input == "scissors" and cptr_pick == "paper":
        print("you won!")
        user_win += 1
    if user_input == "paper" and cptr_pick == "rock":
        print("you won!")
        user_win += 1
    else:
        print("computer won, you lost!")
        cptr_win += 1

print("you won", user_win ,"times")
print("computer won", cptr_win, "times")
print("GOODBYE!")

