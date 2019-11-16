def getAvailableLetters(lettersGuessed):
    list=""
    import string
    availableL=string.ascii_lowercase
    for availL in availableL:
        if availL not in lettersGuessed:
            list= list+ availL
    return (list)
            
    