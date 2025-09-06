def hangman():
    # Small list of predefined words
    words = ["python", "computer", "program", "science", "random"]

    # Randomly choose a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("🎮 Welcome to Hangman!")
    print("Guess the word: ", " ".join(guessed_word))
    print(f"You have {attempts} incorrect guesses allowed.\n")

    # Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        # Check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is in the word
        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word: ", " ".join(guessed_word))
        print("Guessed letters: ", ", ".join(guessed_letters), "\n")

    # Game result
    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
hangman()