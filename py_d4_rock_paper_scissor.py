import random
choice = int(input("What do you want to choose? Type 0 for Rock, 1 for paper & 2 for scissors: "))

options_num = [0,1,2]
options_display = [
#rock 0
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
#paper 1
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
#scissors 2
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

print("You Choose:")
if choice == 0:
    print(options_display[0])
elif choice == 1:
    print(options_display[1])
elif choice == 2:
    print(options_display[2])
else:
    print("Invalid Entry")

print("Computer's Choice:")
comp_choice = random.choice(options_num)
comp_display = options_display[comp_choice]
print(comp_display)

#Match Decider
if options_num[choice] == comp_choice:
    print("Draw")
elif options_num[choice] == 0:
    if comp_choice == 1:
        print("You Loose")
    elif comp_choice == 2:
        print("You Win!")
elif options_num[choice] == 1:
    if comp_choice == 0:
        print("You Win!")
    elif comp_choice == 2:
        print("You Loose")
elif options_num[choice] == 2:
    if comp_choice == 0:
        print("You Loose")
    elif comp_choice == 1:
        print("You Win!")