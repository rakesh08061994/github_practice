# from sys import set_coroutine_origin_tracking_depth


def check_guess(guess,answer):
    '''Quiz game take only one value-guess'''

    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.capitalize() == answer.capitalize():
            print("Correct Answer !")
            score += 1

            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer! Try again : ")
                attempt += 1
            else:
                print("Answer is",answer)
                break


    

score = 0
print("Guess the animal!")

guess1 = input("Which bear lives at the north pole :  ")
check_guess(guess1,'Polar bear')
guess2 = input("Which is fastest land animal !:  ")
check_guess(guess2,'Cheetah')
guess3 = input("Which is the larget animal?:  ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+ str(score))



