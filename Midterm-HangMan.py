import random

hangmanASCII = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']

words = ["cat", "dog", "rabbit", "bird", "fish",
         "elephant", "tiger", "apple", "banana",
         "orange", "grape", "pear", "kiwi",
         "carrot", "potato", "tomato", "onion",
         "broccoli", "spinach", "cucumber", "bag", "phone", "book", "pen", "chair"]


def main():

    # in below code, random word is chosen from words list and printed with '_'
    hidden_word = random.choice(words).strip().lower()
    word_length = len(hidden_word)
    hidden_display = ['_'] * word_length
    counter = 0
    max_attempts = len(hangmanASCII) - 1
    guessed_letters = set()

    print("Welcome to Hangman!")

    while counter < max_attempts:
        print(hangmanASCII[counter])
        print("Word: " + " ".join(hidden_display))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}" if guessed_letters else "")

        guess = input("Guess a letter: ").strip().lower()

        # checking if guess is one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        # revealing guessed letters
        if guess in hidden_word:
            print("Good guess!")
            for i in range(word_length):
                if hidden_word[i] == guess:
                    hidden_display[i] = guess
        else:
            print("Wrong guess!")
            counter += 1

        if '_' not in hidden_display:
            print("\nCongratulations! You Win! :) ")
            print("The word was:", hidden_word)
            return

    print(hangmanASCII[counter])
    print("Game over! You ran out of attempts. :( ")
    print("The word was:", hidden_word)


main()
