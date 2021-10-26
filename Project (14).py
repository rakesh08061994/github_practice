import random
import time
choices = ["Rock", "Paper", "Scissors"]


player = False

cpu_score = 0
player_score = 0

while True:
    computer = random.choice(choices)
    player = input("Rock, Paper or Scissors:   ").capitalize()
    if player == computer:
        print("Match tie!")
    elif player == "Rock":
        if computer == 'Paper':
            print("You loose", computer, "covers ", player)
            cpu_score += 1
        else:
            print("You win", player, 'smashes', computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You loose", computer, 'cuts', player)
            player_score+= 1
        else:
            print("You win", player, ' covers', computer)
            cpu_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You loose", computer, 'smashes', player)
            cpu_score += 1
        else:
            print("You win", player, 'cuts', computer)
            player_score += 1
    elif player == 'Exit':
        print("Thanks to play game \nYour score is Loading...... !")
        time.sleep(3)
        if cpu_score > player_score:
            print("Computer is Overall Winner! ")
            print("cpu score is :",cpu_score)
            print("Player score is",player_score)
            break
        elif cpu_score == player_score:
            print("Match Score tie! ")
            print("cpu score is :",cpu_score)
            print("Player score is",player_score)
            break
        else:
            print("Player is Overall Winner!")
            print("cpu score is :",cpu_score)
            print("Player score is",player_score)
            break

