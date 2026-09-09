import random

words = ["python", "computer", "robot", "programming", "science"]

word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = set()

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in used_letters:
        print("You already guessed this letter.")
        continue

    used_letters.add(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
