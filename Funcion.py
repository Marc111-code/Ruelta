def fiveLines():
    print()
    print()
    print()
    print()
    print()
def cleanScreen():
    for i in range(25):
        print()
def deleteLowercase(p):
    txt = p
    x = txt.upper()
    return x
def isRightLetter(c):
    if c in " bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False
def countWords(p):
    words = p.split()
    llar = len(words)
    if llar <= 3:
        return True
    else: 
        return False 
import string
def isACorrectPanel(p):
    words = p.split()
    llar = len(words)
    if llar > 3:
        return False
    else:
        for paraula in words:
            for lletra in paraula:
                if lletra not in string.ascii_letters:
                    return False
        return True
def secretPanel(p):
    i = "'"
    for paraula in p:
        for lletra in paraula:
            if lletra == " ":
                i = i + " "
            else:
                i = i + "_"
    i+= "'"
    print(i)
def containsLetter(p,c):
    if c in p:
        return True
    else:
        return False
def updateSecretWord(w,sw,c):
    i = 0
    x = ""
    for lletra in w:
        if c == lletra:
            x = x + lletra
            i = i +1
        else:
            x = x + sw[i]
            i = i +1
    return x


import random
def generateNumber():
        return random.randint(0, 5)
