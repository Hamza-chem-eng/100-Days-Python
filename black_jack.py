import random
from typing import final
import art
game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True
while game:
    print(art.logo)
    game = input("Do you want to play ?(y/n): ")
    if game == "y":
        game = True
    else:
        game = False
    player_card = random.choices(cards,k=2)
    print(f"your card: {player_card} , current scor : {sum(player_card)}")
    computer_card = [random.choice(cards)]
    print(f"computer first card: {computer_card} ")
    if sum(player_card) > 21:
        print(f"your final card{player_card} , final scor : {sum(player_card)}")
        print(f"computer final card: {computer_card} , final scor : {sum(computer_card)}")
        print("You lose!😢😢")
    b =True
    while b :
        play_again = input("type (y) to get another card ,type 'n' to pass : ")
        if play_again == "y":
            x = random.choice(cards)
            player_card += [x]
            print(f"your card: {player_card} , current scor : {sum(player_card)}")
            print(f"computer first card: {computer_card} ")
        if play_again == "n":
            b = False
        if 11 in player_card:
            if sum(player_card) > 21:
                player_card.remove(11)
                player_card.append(1)  
        if sum(player_card)  > 21 :
            print(f"your final card{player_card} , final scor : {sum(player_card)}")
            print(f"computer final card: {computer_card} , final scor : {sum(computer_card)}")
            print("You lose!😢😢")
            b = False
    while sum(computer_card) < 17 :
            computer_card.append(random.choice(cards))
    if 11 in player_card :
        if sum(player_card) >21 :
            player_card.remove(11)
            player_card.append(1)
    if 11 in computer_card :
        if sum(computer_card) >21 :
            computer_card.remove(11)
            computer_card.append(1)
    if sum(computer_card) > 21 and sum(player_card) < 21  :
        print(f"player final card: {player_card} , final scor : {sum(player_card)}")
        print(f"computer final card {computer_card} , final scor : {sum(computer_card)}")
        print("you win!")
    if sum(player_card) == 21:
        print(f"your final card{player_card} , final scor : {sum(player_card)}")
        print(f"computer final card: {computer_card} , final scor : {sum(computer_card)}")
        print("perfect win !🥳🥳")
    if sum(player_card) < 21 and sum(computer_card) < 21 :
        final_computer = sum(computer_card)
        final_player = sum(player_card)
        if final_computer < final_player :
            print(f"your final card{player_card} , final scor : {sum(player_card)}")
            print(f"computer final card: {computer_card} , final scor : {sum(computer_card)}")
            print("You win!🤩🤩")
        elif final_player == final_computer :
            print(f"your final card{player_card} , final scor : {sum(player_card)}")
            print(f"computer final card: {computer_card} , final scor : {sum(computer_card)}")
            print("draw🤷‍♂️🤷‍♂️")
        else:
            print(f"your final card{player_card} , final scor : {sum(player_card)}")
            print(f"computer final card: {computer_card} , final scor : {sum(computer_card)}")
            print("you lose!")
