
import random

words = ['juventus', 'handball', 'pokemon', 'artificial', 'nintendo'] # List of words that the player can guess

chosen_word = random.choice(words) #Randomly choose a word from the list
word_display = ['_' for _ in chosen_word] #Create a list of underscores
attempts = 8 #Number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display: # The game continues until either all attempts are used or the player guesses the whole word
    print("\n" + ' '.join(word_display)) # Display the current state of the word (underscores and revealed letters)
    guess = input("Guess a letter: ").lower() # Ask the player to guess a letter and convert it to lowercase to make the game case-insensitive
    if guess in chosen_word: # Check if the guessed letter is in the chosen word
        for index, letter in enumerate(chosen_word): # If the guessed letter is correct, reveal it in the word display
            if letter == guess:
                word_display[index] = guess #Revealing the letter
    else:
        print("That letter does not exist in the word") # If the guessed letter is not in the word, inform the player and decrease the number of attempts
        attempts -= 1


# Game Conclusion
if '_' not in word_display: # If there are no underscores left in word_display, it means the player guessed the word
    print("You guessed the word!")
    print(' '.join(word_display)) # Show the final guessed word
    print("You win!")
else:
    print("You ran out of attempts. The word was " + chosen_word)
    print("You lost!")