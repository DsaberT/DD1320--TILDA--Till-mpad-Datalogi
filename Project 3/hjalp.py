


def putta(trad, x):
    if trad == None:
        nyttord = Node(x)
        trad = nyttord
    if x == trad.value:
        print("Ordet finns redan")
    if x < trad.value:
        return putta(trad.left, x)
    if x > trad.value:
        return putta(trad.right, x)

def finns(trad, value):
    if trad == None:
        return False
    if value == trad.value:
        return True
    if value < trad.value:
        return finns(trad.left, value)
    if value > trad.value:
        return finns(trad.right, value)

def skriv(trad):
    if trad != None:
        skriv(trad.left)
        print(trad.value)
        skriv(trad.right)
