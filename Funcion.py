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


def updatePoints(sw,c):
    i = 0
    for lletra in sw:
        if lletra == c:
            i  =  i + 1
    return i

def correctPanel(w,sol):
    if w == sol:
        return True
    else:
        return False


def game():
    jugadorB = 0
    jugadorC = 0
    torn = "B"
    topic = input("Jugador A, inserta el tema del panell secret: ")
    secret = input("Jugador A, inserta el panell secret: ")
    cleanScreen()
    print("Juguem!")
    print("El tema del panell secret és: " + topic)
    
    print("Torn de: " + torn)
    print("La jugada dona "+ str(generateNumber()) + " punts")
    print("El panell secret per revelar és: " + secretPanel(secret))
    res1 = input("Vols resoldre el panell? (Y/N): ")
    if res1 == "N" or res1 == "n":
        lletP = input("Inserta la lletra: ")
        if lletP in secret:
            print(updateSecretWord(secret,secretPanel(secret),lletP))
            if torn == "B":
                torn == "B"
            if torn == "C":
                torn == "C"
            print("Turn of Player "+ torn)
        else:
            print("La solució és: "+ secret)
            if torn == "B":
                torn == "C"
            if torn == "C":
                Torn == "B"
            print("Torn de: " + torn)
game()
