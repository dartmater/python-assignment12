def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ''.join([l if l in guesses else '_' for l in secret_word])
        print(display)
        return set(secret_word).issubset(set(guesses))

    return hangman_closure

if __name__ == "__main__":
    word = input("Enter secret word: ").lower()
    game = make_hangman(word)
    while True:
        guess = input("Guess a letter: ").lower()
        if game(guess):
            print("You won!")
            break
