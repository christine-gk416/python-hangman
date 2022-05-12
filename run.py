from random import choice

# secret word that player is trying to guess
secretWord = choice(['compose','assignment','weave','filter','swell','baby','property','north','ward','rack','boot','psychology'])

name = input("What is your name? ")
# Here the user is asked to enter the name first


def playGame():

    print(f"Good Luck! {name}")
    
    print("Let's play Hangman!")
    lettersGuessed = ''
    # the number of turns before player loses
    failureCount = 6
    print(display_hangman(failureCount))

    while failureCount > 0:
        guess = input('Enter a letter: ')

        if guess in secretWord:
            print(f'Correct there is one or more {guess} in the secret word.')
        else:
            failureCount -= 1
            print(f'Incorrect. There are no {guess} in secret word. {failureCount} turn(s) left.')
            print(display_hangman(failureCount))
        
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


def display_hangman(failureCount):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[failureCount]

def main():
    playGame()
    while input("Play Again? (Y/N) ").upper() == "Y":
        
        playGame()

main()