import random

# List of words to choose from, with hints
words = [
    {"word": "apple", "hint": "A type of fruit"},
    {"word": "banana", "hint": "A yellow curved fruit"},
    {"word": "cherry", "hint": "A small red fruit"},
    {"word": "date", "hint": "A type of fruit often eaten on special occasions"},
    {"word": "elderberry", "hint": "A type of fruit used to make jam"},
    {"word": "fig", "hint": "A sweet fruit often eaten dried"},
    {"word": "grape", "hint": "A type of fruit often used to make wine"}
]

# Choose a random word from the list
word_info = random.choice(words)
word = word_info["word"]
hint = word_info["hint"]

# Create a list to store the guessed letters
guessed = ['_'] * len(word)

# Set the limit of incorrect guesses
limit = 6

# Initialize the number of incorrect guesses
incorrect_guesses = 0

print("Welcome to Hangman!")
print("You have", limit, "chances to guess the word.")
print("To play, simply type a letter and press Enter.")
print("If you guess a letter correctly, it will be revealed in the word.")
print("If you make an incorrect guess, I'll let you know and you'll lose a chance.")
print("Your goal is to guess the word before you run out of chances!")
print("")
print("Here's a hint to help you get started:")
print(hint)
print("The word has", len(word), "letters.")
print("")

while True:
    # Print the current state of the word
    print(' '.join(guessed))

    # Ask the user for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is in the word
    if guess in word:
        # Reveal the correctly guessed letters
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good job! You guessed a letter correctly.")
    else:
        # Increment the number of incorrect guesses
        incorrect_guesses += 1
        print("Oops, that's not correct. You have", limit - incorrect_guesses, "chances left.")

    # Check if the word has been fully guessed
    if '_' not in guessed:
        print(' '.join(guessed))
        print("Congratulations, you won! The word was", word)
        break

    # Check if the limit of incorrect guesses has been reached
    if incorrect_guesses == limit:
        print("You lost! The word was", word)
        break