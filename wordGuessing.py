import random
name=input("Enter your name:")
print("Good Luck!",name)
words=['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer',
       'function', 'variable', 'condition', 'loop', 'array', 'string', 'integer',
       'water', 'computer', 'science', 'keyboard', 'internet', 'software', 'hardware']
word=random.choice(words)
print("Guess the word:")

guess=''
turns=21
while turns>0:
    failed=0
    for char in word:
        if char in guess:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed+=1
    print()
    if failed==0:
        print("Congratulations! You guessed the word:", word)
        break
    letter=input("Guess a letter: ")
    guess+=letter
    if letter not in word:
        turns-=1
        print("Wrong guess.")
        print("You have", turns, "more guesses.")
        if turns==0:
            print("Sorry, you lost. The word was:", word)
