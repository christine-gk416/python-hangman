from random import choice

# secret word that player is trying to guess
secretWord = choice(['compose','assignment','weave','filter','swell','baby','property','north','ward','rack','boot','psychology'])

name = input("What is your name? ")
# Here the user is asked to enter the name first
 
print("Good Luck! ", name)

def playGame():
    lettersGuessed = ''
    # the number of turns before player loses
    failureCount = 12
    while failureCount > 0:
        guess = input('Enter a letter: ')

        if guess in secretWord:
            print(f'Correct there is one or more {guess} in the secret word.')
        else:
            failureCount -= 1
            print(f'Incorrect. There are no {guess} in secret word. {failureCount} turn(s) left.')
        
        lettersGuessed = lettersGuessed + guess
        wrongLetterCount = 0

        for letter in secretWord:
            if letter in lettersGuessed:
                print(f'{letter}', end='')
            else:
                print(f'_', end='')
                wrongLetterCount += 1
        print('')

        if wrongLetterCount == 0:
            print(f'Congratulations! The secret word was {secretWord}. You won!')
            break

    else:
        print(f'Sorry you did not win, but try again.')


playGame()