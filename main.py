import random
import string
import sys


def is_playing():
    word = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if word == "play":
        play()
    elif word == "exit":
        pass
    else:
        is_playing()


def compare(original, guess):
    return original == guess


def update_list(ltr, wrd, hidden_list):
    for i in range(len(wrd)):
        if ltr == wrd[i]:
            hidden_list[i] = ltr
    return hidden_list


def is_valid(ltr):
    if len(ltr) < 1 or len(ltr) > 1:
        return False
    else:
        return True


def is_lowercase(ltr):
    return ltr in string.ascii_lowercase


def play():
    words = ["python", "java", "kotlin", "javascript"]
    prev_letter = []
    effort = 8
    word = random.choices(words).pop()
    hidden_words = ["-" for x in range(len(word))]

    while effort > 0:
        print("\n" + "".join(hidden_words))
        letter = input("Input a letter: ")
        is_val = is_valid(letter)
        is_lower = is_lowercase(letter)
        if not is_val:
            print("You should input a single letter")
        elif not is_lower:
            print("Please enter a lowercase English letter")
        elif letter in word and letter not in hidden_words:
            hidden_words = update_list(letter, word, hidden_words)
        elif letter in hidden_words or letter in prev_letter:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            effort -= 1
        guess_wrd = "".join(hidden_words)
        prev_letter.append(letter)
        if word == guess_wrd:
            break

    guess_word = "".join(hidden_words)
    is_same = compare(word, guess_word)
    if is_same:
        print(word + f"\nYou guessed the word {guess_word}!\nYou survived!\n")
        is_playing()
    else:
        print("You lost!\n")
        is_playing()


sys.setrecursionlimit(1000000)
print("H A N G M A N")
is_playing()
