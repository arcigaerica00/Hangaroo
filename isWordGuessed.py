def isWordGuessed(secretWord,lettersGuessed):
    tester=0
    for letterS in secretWord:
        for letterL in lettersGuessed:
            if letterL==letterS:
                tester+=1
            else:
                return False
            return True