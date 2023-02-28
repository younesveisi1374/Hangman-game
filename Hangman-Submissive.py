# This program is written by Younes Vesey

# Import libraries
import random
from words import words

# A function to receive and control the selected word


def get_word():
    word = random.choice(words)
    return word.upper()

# Main game execution function


def play(word):
    # Convert the number of letters of the main word to spaces
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    # A brief introduction
    my_name = input("\nPlease Enter your Name: ")
    print("Hi", my_name.capitalize(), "Welcome to hangman game.")
    print("\nLet's play the Game!")
    # Calling the show hangman function
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        # Enter the guess word
        guess = input("Please guess a letter or word: ").upper()
        # Checking the entered letter with capital letters
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guesseed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                if tries > 0:
                    print("You can try "+str(tries)+" time.")
                else:
                    print("Your efforts are over!")
                guessed_letters.append(guess)
            else:
                print("good job", guess, "is the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indicates = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indicates:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                if tries > 0:
                    print("You can try "+str(tries)+" time.")
                else:
                    print("Your efforts are over!")
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # A condition for the message to win the game
    if guessed:
        print("Congrats ", my_name, ", you guessed the word! You Win!")
    else:
        print("Sorry, you ran out of tries. thw word was *** " +
              word+" *** .Maybe next time.")

# The function to display the shape of the game hangman


def display_hangman(tries):
    stages = ["""
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / \\
                 -
                 """,
              """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / 
                 -
                 """,
              """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     
                 -
                 """,
              """
                 --------
                 |      |
                 |      O
                 |     \\|
                 |      |
                 |     
                 -
                 """,
              """
                 --------
                 |      |
                 |      O
                 |      |
                 |      |
                 |     
                 -
                 """,
              """
                 --------
                 |      |
                 |      O
                 |     
                 |     
                 |     
                 -
                 """,
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
    return stages[tries]

# Main function


def main():
    word = get_word()
    play(word)


# main function to call the entire program
if __name__ == "__main__":
    main()
