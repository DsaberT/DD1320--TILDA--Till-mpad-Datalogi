from bintreeFile import *
from linkedQfile import *

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, barn):
        if barn.parent == None:
            print(barn.word)
        else:
            self.writechain(barn.parent)
            print(barn.word)


def sve():
    svenska = Bintree()                                 #given kod för att kolla om ens kod funkar
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)             # in i sökträdet
    return svenska

def makeChildren(test, svenska, q, gamla):
    gamla.put((test.word))
    abc = "abcdefghijklmnopqrstuvwxyzåäö"
    for i in range(0, len(test.word)):
        ordarray = []
        for b in test.word:
            ordarray.append(b)
        for c in abc:
            ordarray[i] = c
            nyttord = "".join(ordarray)
            if nyttord in svenska:
                if nyttord not in gamla:
                    gamla.put(nyttord)
                    nynod = ParentNode(nyttord)
                    nynod.parent = test
                    q.enqueue(nynod)

                else:
                    pass
            else:
                pass





