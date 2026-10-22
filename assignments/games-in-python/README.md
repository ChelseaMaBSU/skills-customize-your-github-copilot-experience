
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python. Practice string manipulation, loops, conditionals, user input, and random selection while tracking the player's progress.

## 📝 Tasks

### 🛠️ Build the Game Setup

#### Description

Use the provided starter code to select a secret word and initialize the variables needed to track guessed letters, incorrect guesses, and the maximum number of incorrect guesses.

#### Requirements

Completed program should:

- Select a word randomly from the provided `words` list.
- Create a way to store the player's guessed letters.
- Set a maximum number of incorrect guesses and track the remaining attempts.

### 🛠️ Implement the Guessing Game

#### Description

Create the main game loop. Ask the player for letter guesses, update the displayed word progress, and end the game when the word is guessed or the player runs out of attempts.

#### Requirements

Completed program should:

- Display the current progress using underscores for letters that have not been guessed.
- Accept letter guesses and update the progress when a guessed letter is in the secret word.
- Track incorrect guesses and display the number of attempts remaining.
- End when the player guesses the complete word or uses all allowed incorrect guesses.
- Display a clear win or lose message at the end of the game.
