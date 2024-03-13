import random   
import os
import time


def run():

    print("Welcome to Hangman, let's play!")
    
    print(r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/   
    """)
    time.sleep(3)
    IMAGES = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r''' 
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


    DB = [
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "C",
        "PHP",
        "RUBY",
        "SWIFT",
        "KOTLIN",
        "OBJECTIVEC",
        "GO",
        "TYPESCRIPT",
        "SCALA",
        "RUST",
        "COBOL",
        "PERL",
        "LUA",
        "HTML",
        "CSS",
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attempts = 0

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")   
        print(IMAGES[attempts])    
        letter = input("Choose a letter: ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        
        if not found:
            attempts += 1

        if "_" not in spaces:
            os.system("clear")
            print("You win!")
            break
        
        if attempts == 6:
            os.system("clear")
            print("You lose!")
            break

if __name__ == '__main__':
    run()
