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
    
