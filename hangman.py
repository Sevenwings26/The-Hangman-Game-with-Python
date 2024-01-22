# The Hangman Word Prediction game 
# Using Chart

#Import libraries
import hangman_art
import hangman_words
import random

print (hangman_art.logo)

#Generate random word from the hangman_words 
chosen_word = random.choice(hangman_words.word_list)
print(f"The Selected word is {chosen_word}")

game_lives = 6

end_of_game = False

#Generate as many blanks in the chosen_words

display = []

for _ in chosen_word:
    display += "_"
print(display) 

# while not end_of_game:
while end_of_game != False:
    
    guess = input("Guess a letter: ")
    # print(f"You have guessed letter '{guess}'.")

    if guess in display:
        print(f"You have guessed letter '{guess}'.").lower() 
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
                
    if guess not in chosen_word:
        print(f"'{guess}' you guessed is not in the chosen word. You have lose a life.")
        game_lives -= 1
        if game_lives == 0:
            end_of_game = True
            print("Game over. You lose.")
            
    print(f"{' '.join(display)}")
            
    if "_" not in display:
            end_of_game = True
            print("You win!")
    print(hangman_art.stages[game_lives])
    