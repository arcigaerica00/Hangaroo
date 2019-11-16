def getGuessedWord(secretWord,lettersGuessed):
    gword=""
    for letterS in secretWord:
        if letterS in lettersGuessed:
            gword=gword+letterS
        else:
            gword= gword + "_"
    return gword
        
        