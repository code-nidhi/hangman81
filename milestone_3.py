import random
#imports package, this needs to be at the top of the project

#creates word list
word_list = ["mango", "pear", "banana", "grape", "strawberry"]
print(word_list)

#chooses a random word from word_list
word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess.lower()
    #if-else statement checks if the letter the user inputted is in the randomly chosen word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    #while loop checks if the user input is a single alphabetical letter
    while True:
        guess =  input("Please enter a letter")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    #calls check_guess function outside while loop 
    check_guess(guess)   

# ask_for_input()