import random
from hangman_words import word_list
from stages import stages

chosen_word = random.choice(word_list)
#print(chosen_word)
lives = 6


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"You Have {lives}/6 lives left")
    guess = input("Guess a letter: \n"). lower()
    
    if guess in correct_letters:
        print(f"You already guess {guess}")
    
    
    display = ""
  
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)
    
    if guess not in correct_letters:
        lives -= 1
        print(f"You have guessed {guess}, that is not in the word. You lose a life,")
    
     
    print(stages[lives])

    
    if "_" not in display:
        game_over = True
        print("You Win")
    if lives == 0:
        game_over = True
        print(f"You Lose.The correct words was {chosen_word}")