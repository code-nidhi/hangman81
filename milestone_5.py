import random
#imports package random needed to randomly select a word

class Hangman: 
    """
    This class is used to play a game of Hangman.

    Attributes:
        word_list (list): a list of words
        num_lives (int): the number of lives that the player has
        word (str): the word that the player will attempt to guess, chosen randomly from word_list
        word_guessed (list): blank spaces with a space for every letter to be guessed
        num_letters (int): the number of unique letters in the word which have not yet been guessed
        list_of_guesses (list): the letters that the player has already guessed
    """
    def __init__(self, word_list=["mango", "pear", "banana", "grape", "strawberry"], num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = str(random.choice(word_list))
        self.word_guessed = []
        for item in self.word:
            self.word_guessed.append("_")
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def play_game(self, word_list):
        """
        This function should be called to begin the game of Hangman.
        If the number of lives becomes zero, the function tells the player they have lost.
        While the number of lives is greater than zero, the function calls the ask_for_input() function.
        If the number of lives is greater than zero, and there are no letters left to guess, the function tells the player they have won the game.

        Args:
            word_list (list) = a list of words
        """
        while True:
            if self.num_lives == 0:
                print("You lost!")
                break
            if self.num_lives > 0:
                self.ask_for_input()
            if self.num_lives > 0 and self.num_letters == 0:
                print("Congratulations. You won the game!")
                break

    def check_guess(self, guess):
        """
        This function is used to check whether the guess that the player has inputted is in the word.
        First, it ensures that the guess is lowercase (which is important due to case sensitivity).
        If the guess is in the word, it replaces the blank in word_guessed.
        If the guess is not in the word it tells the player this.

        Args:
            guess (str): a single alphabetical character inputted by the player
        """
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.num_letters -= 1
            print(self.num_letters)
            # uses enumerate to ensure all instances of a letter are entered into word_guessed
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
                    print(self.word_guessed)    
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
        
    def ask_for_input(self):
        """
        This function asks the player to input a value. 
        It then has a set of conditions to check whether this fits the criteria of being a single alphabetical character.
        When the user input fits this criteria, it calls the function check_guess.
        """   
        guess = input("Please input a letter")
        if len(guess) != 1  or guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)
                
#creates and instance of the Hangman class
game = Hangman(["mango", "pear", "banana", "grape", "strawberry"], 5)
#calls the play_game function
game.play_game(["mango", "pear", "banana", "grape", "strawberry"])