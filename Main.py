#Config
lives = 5
#Main
wordInput = input("What word shall this hangman be?")
wordInputLength = len(wordInput)
Dashes = ""
for x in wordInput:
    if x == " ":
        Dashes = Dashes + " "
    else:
        Dashes = Dashes + "_"
print(Dashes)
for x in wordInput:
    if not x == " ":
        Guess = input("Guess?")
        if Guess in wordInput:
            print("Correct: " + Guess)
        else:
            lives -= 1
            print("Incorrect! " + str(lives) + " lives left.")
#end
if lives > 0:
    print("You win good job! The word was: " + wordInput)
else:
    print("Try better next time. The word was: " + wordInput)
