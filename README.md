# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

This implementation asks the user to input a single alphabetical letter. It then defines a function to check the validity of the input, checking if it is indeed a letter and a lone one at that. 

The function then checks whether the letter inputted by the user is in the word that the computer has randomly generated. It also accounts for repetition. The check_guess() function lowers the number of lives for every incorrect guess. The ask_in_input() function calls the check_guess() function. 

