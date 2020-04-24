def start():
    import random
    number = random.randint(1, 10)
    # number = 2
    guessCount = 0
    guessLimit = 3
    # print(number)
    while guessCount < guessLimit:
        guess = int(input(f'Your {guessCount + 1}st guess>>> '))

        if guess > number and guessCount != 2:
            print('Just a bit lower..')
        elif guess < number and guessCount != 2:
            print('Just a bit higher..')
        if guess == number:
            print('You got it.')
        elif guessCount == 2 and number != guess:
            print('You lost the game.')
            print(f'Secret number was {number}.')
        guessCount += 1
    playAgain = input('Do you want to play again? [Y/N]')
    if playAgain.upper() == 'Y':
        print('')
        print('Good luck with your luck')
        start()
    elif playAgain.upper() == 'N':
        pass
try:
    start()
except(ValueError):
    print('Only numbers are allowed')