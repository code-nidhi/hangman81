# Hangman

### Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

This implementation asks the user to input a single alphabetical letter. It defines a function ask_for_input() to check the validity of the input, checking if it is indeed a letter and a lone one at that. 

The ask_for_input() function calls the check_guess() function. The check_guess() function checks whether the letter inputted by the user is in the word that the computer has randomly generated. It also accounts for repetition. The check_guess() function lowers the number of lives for every incorrect guess.

The game is implemented in the first place with the function play_game(). This calls the ask_for_input() function if the player has a positive number of lives. The function is also responsible for telling the player if and when they win or lose the game of Hangman.

The file milestone_5 shows the full Hangman class, while the milestones before show earlier forms of the check_guess() and ask_for_input() functions.

I had to take care when using while loops whilst creating these functions. I initally encountered a problem where the num_lives variable continued to reduce below zero due to a misplaced while loop.

### Usage
The Hangman class is designed to take a word list as a parameter and number of lives as a parameter. When creating an instance of the Hangman class, these parameters allow the class to be adapted so that the list itself can be of any length and the list may contain words of varying lengths. In addition, we may change the number of lives. Both of these parameters allow the user to alter the game's difficulty level.

### License
Unlicense