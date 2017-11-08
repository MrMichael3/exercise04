secret_word = input("What is the secret word?")
guesses = int(input("How many tries is the Player allowed to have?"))
print("The secret word has %d characters" %(len(secret_word)))
print("You have %d tries left." % guesses)

word = []
counter = len(secret_word)
while counter > 0:  # Liste mit _ erstellen
    counter -= 1
    word.append("_")
for x in word:
    print(x, end=" ")
print("\n")

guessed_words = []
while guesses > 0:
    counter = -1
    guess = input("guess one letter of the alphabet: ")
    # already guessed letter
    if guess in guessed_words:
        print("Oops! You have already guessed this letter!")
    # correct letter
    elif guess in secret_word:
        for letter in secret_word:
            counter += 1
            if letter == guess:
                word[counter] = guess
        print("Nice guess, this letter is in the secret word!")
        guesses -= 1    # in dem Beispiel wird auch bei richtigem Buchstaben ein guess abgezogen
    # wrong letter
    else:
        guesses -= 1
        print("Oops, this letter is not in the word!")

    guessed_words.append(guess)
    if "_" not in word:
        print("Congratulations, you have guessed the word %s!" %secret_word)
        break
    if guesses == 0:
        print("You have no try left, Game over!")
        break
    print("you have %d tries left" % guesses)
    for x in word:
        print(x, end=" ")
    print("\n")


def guess_1():
"""    
     
    
    
    
    
    
    
    
    
    """"