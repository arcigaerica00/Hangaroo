def isWordGuessed(secretWord,lettersGuessed):
    tester=0
    for letterS in secretWord:
        for letterL in lettersGuessed:
            if letterL==letterS:
                tester+=1
            else:
                return False
            return True
def getGuessedWord(secretWord,lettersGuessed):
    gword=""
    for letterS in secretWord:
        if letterS in lettersGuessed:
            gword=gword+letterS
        else:
            gword= gword + "_ "
    return gword
        
def getAvailableLetters(lettersGuessed):
    list=""
    import string
    availableL=string.ascii_lowercase
    for availL in availableL:
        if availL not in lettersGuessed:
            list= list+ availL
    return (list)
            
def Hangaroo(secretWord):
    import string
    availableL=string.ascii_lowercase
    lettersGuessed = []
    list(lettersGuessed)
    mistakesMade = 0
    
    print("Let's Play Hangaroo!")
    print("The word is " +  str(len(secretWord))  + " letters long.")
    print("You have made",mistakesMade,"mistakes!")
    print(getGuessedWord(secretWord,lettersGuessed))
    
    
    while mistakesMade < 100000000000:
        if isWordGuessed(secretWord, lettersGuessed):
            return print("Awesome! You got the word right!")
    
        print("Available letters: " + getAvailableLetters(lettersGuessed))
            
        guess = input("Type a letter that will fit the word: ")
        guess = str(guess)
        guess = guess.lower()
        
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            
            if guess in secretWord:
                print("You got a letter right! Way to go!")
            else:
                mistakesMade += 1
                print("Nope!Try again!")
                print("You have made",mistakesMade,"mistakes!")
        else:
            print("You already tried that letter!")

    return print("You ran out of guesses. The word was " + str(secretWord))

