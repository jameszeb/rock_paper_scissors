from random import randrange

class rps_checker:
    answer = ''


    def number_checker(answer):

        if answer == 0:
            answer = 'rock'
        if answer == 1:
            answer = 'paper'
        if answer == 2:
            answer = 'scissors'
        print(f'\nChecking computers answer ... {answer}')
        return answer

rps = rps_checker

rock = 'rock'
paper = 'paper'
scissors = 'scissors'


print(f'Welcome to {rock}, {scissors}, {paper}!')




play_the_game = True
wins = 0
losses = 0
ties = 0

while play_the_game:
    choice = input('\nWhich would you like to do?')
    computer_choice = randrange(0, 2)
    rps.answer = computer_choice
    computer_choice = rps.number_checker(computer_choice)


    if choice == rock and computer_choice == paper:
        print(f'\nYou chose {rock} and the computer chose {paper}.')
        play_again = input('\nYou Lost! Play again?')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        losses += 1

    if choice == rock and computer_choice == scissors:
        print(f'\nYou chose {rock} and the computer chose {scissors}.')
        play_again = input('\nYou won!Play again?')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        wins += 1

    if choice == rock and computer_choice == rock:
        print(f'\nYou chose {rock} and the computer chose {rock}.')
        play_again = input('\nIt\'s a tie! Play again?')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        ties += 1

    if choice == paper and computer_choice == scissors:
        print(f'\nYou chose {rock} and the computer chose {scissors}.')
        play_again = input('\nYou Won! Play again?: ')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        losses += 1

    if choice == paper and computer_choice == rock:
        print(f'\nYou chose {paper} and the computer chose {rock}.')
        play_again = input('\nYou Won!Play again?: ')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        wins += 1

    if choice == paper and computer_choice == paper:
        print(f'\nYou chose {paper} and the computer chose {paper}.')
        play_again = input('\nIt\'s a tie! Play again?: ')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        ties += 1

    if choice == scissors and computer_choice == rock:
        print(f'\nYou chose {scissors} and the computer chose {rock}.')
        play_again = input('\nYou lost!Play again?')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        losses += 1

    if choice == scissors and computer_choice == paper:
        print(f'\nYou chose {scissors} and the computer chose {paper}.')
        play_again = input('\nYou won!Play again?: ')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        wins += 1

    if choice == scissors and computer_choice == scissors:
        print(f'\nYou chose {scissors} and the computer chose {scissors}.')
        play_again = input('\nIt\'s a tie!?Play again?: ')
        if play_again == 'n' or play_again == 'no':
            play_the_game = False
        ties += 1
print(f"The current score is... ")
print(f"wins: {wins} ")
print(f"losses:  {losses} ")
print(f"ties:  {ties} ")



