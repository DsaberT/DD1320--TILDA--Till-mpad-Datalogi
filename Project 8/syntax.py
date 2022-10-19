from linkedQfile import *

class Syntaxfel(Exception):
    pass


def lagring(strang):
    q = LinkedQ()
    Mlist = list(strang)

    for i in range(len(Mlist)):
        q.enqueue(Mlist[i])
    return q

def Molekyl(strang):
    lista = lagring(strang)
    first = lista.dequeue()

    if lista.isEmpty() == True:
        return Atom(first)
    elif not Atom(first) == True:
        return Atom(first)
    else:
        pass

    second = lista.peek()
    if not sifferkoll(second) == True:
        second = lista.dequeue()
        if lista.isEmpty():
            return (Atom(first + second))
        elif not Atom(first + second) == True:
            return Atom(first + second)
        else:
            pass
    sum = ""
    while lista.isEmpty() == False:
        sum = sum + str(lista.dequeue())
    return Nummer(sum)

def Atom(strang):
    lista = list(strang)
    if len(lista) > 2:
        try:
            raise Syntaxfel("Atom kan inte vara "+ str(len(lista))+ " Lång.")
        except Syntaxfel as Fel:
            return str(Fel)
    elif len(lista) == 1:
        if StorBokstav(lista[0]):
            return True
        try:
            raise Syntaxfel(lista[0] + " Är inte en stor bokstav")
        except Syntaxfel as Fel:
            return str(Fel)
    elif len(lista) == 2:
        if not StorBokstav(lista[0]) == True and not LitenBokstav(lista[1]) == True:
            try:
                raise Syntaxfel(lista[0] + " Är inte en Storbokstav och "+ lista[1]+ " Är inte en litenbokstav")
            except Syntaxfel as Fel:
                return str(Fel)
        else:
            if not StorBokstav(lista[0]):
                try:
                    raise Syntaxfel(lista[0]+" Är inte en stor bokstav")
                except Syntaxfel as Fel:
                    return str(Fel)
            elif not LitenBokstav(lista[1]):
                try:
                    raise Syntaxfel(lista[1]+" Är inte en liten bokstav")
                except Syntaxfel as Fel:
                    return str(Fel)
            else:
                return True

def StorBokstav(Bokstav):
    storbokstav = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if Bokstav in storbokstav:
        return True
    return False

def LitenBokstav(Bokstav):
    smabokstav = "abcdefghijklmnopqrstuvwxyz"
    if Bokstav in smabokstav:
        return True
    return False

def sifferkoll(siffra):
    try:
        siffra = int(siffra)
        return True
    except ValueError:
        return False

def Nummer(siffra):
        try:
            siffra = int(siffra)
            if siffra > 1:
                return True
            else:
                try:
                    raise Syntaxfel(str(siffra) + " är mindre än 2")
                except Syntaxfel as Fel:
                    return str(Fel)
        except ValueError:
            return (str(siffra) + " är ingen siffra och innehåller andra tecken")


q = LinkedQ()
for a in "ab":
    q.enqueue(a)

print(Atom("a"))
