# This program is written by Younes Vesey
# Import libraries
import random
from words import words
# An empty list to display the names of the winner(s).
winner_list = []

# Game performance class


class HangmanPlayer:
    # Class variable
    player_list = []
    #

    def __init__(self):
        self.name = input("\nPlease Enter your Name: ")
        self.tries = 6
        self.__word = random.choice(words)
        self.__win_state = False
        self.player_list.append(self)

    # Main game execution function

    def play(self):
        # Variable type conversion
        word = str(self.__word)
        myword = word.upper()
        # Convert the number of letters of the main word to spaces
        word_completion = "_" * len(myword)
        guessed_letters = []
        guessed_words = []
        # A brief introduction
        print("Hi", self.name.capitalize(), "Welcome to hangman game.")
        print("\nLet's play the Game!")
        # Calling the show hangman function
        print(self.display_hangman())
        print(word_completion)
        print("\n")
        """ A for loop to match the letters
        entered by the user with the letters
        of the original word"""
        while not self.__win_state and self.tries > 0:
            # Enter the guess word
            guess = input("Please guess a letter or word: ").upper()
            # Checking the entered letter with capital letters
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guesseed the letter", guess)
                elif guess not in myword:
                    print(guess, "is not in the word")
                    self.__guess_left()
                    self.has_guess_left()
                    guessed_letters.append(guess)
                else:
                    print("good job", guess, "is the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indicates = [i for i, letter in enumerate(
                        myword) if letter == guess]
                    for index in indicates:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        self.__win_state = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != myword:
                    print(guess, "is not the word.")
                    self.__guess_left()
                    self.has_guess_left()
                    guessed_words.append(guess)
                else:
                    self.__win_state = True
                    word_completion = myword
            else:
                print("Not a valid guess.")
            print(self.display_hangman())
            print(word_completion)
            print("\n")

        # A condition for the message to win the game
        if self.__win_state:
            winner_list.append(self.name.capitalize())
            print("Congrats", self.name.capitalize(),
                  ", you guessed the word! You Win!")
        else:
            """Note: In the negative condition,
            if the win status does not change and remains False,
            after the end of the game, the program will experience an infinite loop,
            which will only happen for the first time when there is no winner."""
            self.__win_state = True
            print("Sorry, you ran out of tries. thw word was *** " +
                  myword+" *** .Maybe next time.")

    # Function reducing the number of attempts

    def __guess_left(self):
        self.tries -= 1

    # Function indicating the number of remaining chances

    def has_guess_left(self):
        if self.tries > 0:
            print("You can try "+str(self.tries)+" time.")
        else:
            print("Your efforts are over!")

    # The function of changing the state of winning and losing the game

    def has_won(self):
        return self.__win_state

    # The function to display the shape of the game hangman

    def display_hangman(self):
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
        return stages[self.tries]

    # The function that determines the winner of the game
    @classmethod
    def winner_game(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False

# Game controller class


class GameController(HangmanPlayer):
    def __init__(self):
        while True:
            for player in HangmanPlayer.player_list:
                if not player.has_won():
                    player.play()
            if HangmanPlayer.winner_game():
                break

# The function of displaying game commands


def main():
    while True:
        order = input(
            "what do you want to do?(enter number)\n1- add\n2- start\n3- exit\norder: ")
        if order == "1":
            HangmanPlayer()
        elif order == "2":
            GameController()
        elif order == "3":
            print("\nThe names of the winners of the game:\n",
                  "\n".join(winner_list))
            break


# main function to call the entire program
if __name__ == "__main__":
    main()
