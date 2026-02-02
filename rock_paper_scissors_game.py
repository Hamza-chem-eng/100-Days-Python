rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
ist = [rock, scissors, paper]
comp = random.choice(ist)
print("Welcome to the Rock Paper Scissors game!")
player = int(input("write 0 to choice rock,1 to paper and 2 to scissors: "))
if player == 0:
    print("You chose :")
    print(rock)
    print(f"the computer chose :{comp}")
    if comp == rock:
        print("draw")
    elif comp == paper:
        print("you lose")
    elif comp == scissors:
        print("you win")
elif player == 1:
    print("you chose :")
    print(paper)
    print(f"the computer chose  :{comp}")
    if comp == paper:
        print("draw")
    elif comp == rock:
        print("you win")
    elif comp == scissors:
        print("you lose")
else :
    print("you choice :")
    print(scissors)
    print(f"the computer chose :{comp}")
    if comp == rock:
        print("you lose")
    elif comp == paper:
        print("you win")
    elif comp == scissors:
        print("draw")
