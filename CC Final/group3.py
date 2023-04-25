import random

def choose_word():
    words = ['python', 'game', 'play', 'word', 'guess']
    return random.choice(words)

def play_game(word):
    guesses = []
    tries = 6

    while tries > 0:
        print("Word:", ' '.join([c if c in guesses else '_' for c in word]))

        guess = input("Enter a letter: ").lower()

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.append(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect! Tries left:", tries)

        if all(c in guesses for c in word):
            print("Congratulations! You guessed the word:", word)
            return

    print("Game over! The word was:", word)

def main():
    print("Welcome to Hangman!")
    word = choose_word()
    play_game(word)

if __name__ == "__main__":
    main()
