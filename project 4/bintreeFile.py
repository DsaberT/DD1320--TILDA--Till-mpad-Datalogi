
class Node:
    def __init__(self, value):                                  # skapar en node för att spara värden, och tfå pekare åt
        self.value = value                                      # vänster och höger
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder

        skriv(self.root)
        print("\n")

def putta(trad, x):
    nyttord = Node(x)
    if trad == None:
        return nyttord
    if x < trad.value:
        if trad.left == None:
            trad.left = nyttord
        else:
            putta(trad.left, x)
    if x > trad.value:
        if trad.right == None:
            trad.right = nyttord
        else:
            putta(trad.right, x)
    return trad

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
