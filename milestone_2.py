import random
#imports package, this needs to be at the top of the project

#creates word list
word_list = ["mango", "pear", "banana", "grape", "strawberry"]
print(word_list)

#chooses a random word from word_list
word = random.choice(word_list)
print(word)

#asks user to input a single letter
guess = input("Please input a single letter")
#print(guess)

#checks if user input for guess is a valid
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")