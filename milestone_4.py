import random

class Hangman: 
    def __init__(self, word_list=["mango", "pear", "banana", "grape", "strawberry"], num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = str(random.choice(word_list))
        self.word_guessed = ["_", "_", "_", "_", "_"]
        self.num_letters = len(set(self.word_guessed))
        self.list_of_guesses = []
        #self.guess = str()
    
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    letter = self.word_guessed.index(letter)
                else:
                    self.num_lives =- 1
                    print(f"Sorry, {letter} is not in the word.")
                    print(f"You have {self.num_lives} left.")
            self.num_letters =- 1
        
    def ask_for_input(self):
        while True:
            guess = input("Please input a letter")
            if len(guess) != 1  or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
            
my_instance = Hangman(["mango", "pear", "banana", "grape", "strawberry"], 5)
print(my_instance.ask_for_input())