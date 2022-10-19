from songclass import *
from sokfunk import *
import timeit


def main1(n):
    fil = "unique_tracks.txt"
    list = readfile(fil)

    print("Antal element =", n)
    list = list[0:n]
    sista = list[n-1]

    testartist = sista.songnamn

    linjtid = timeit.timeit(stmt = lambda: linsok(list, testartist), number = 1000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")


    lista = sortlista(list)

    bintid = timeit.timeit(stmt = lambda: binsearch(lista, testartist), number = 1000)
    print("binärsökningen tog", round(bintid, 4) , "sekunder")

    Hash = Hashdict(list)

    hashtid = timeit.timeit(stmt = lambda: Hashsok(Hash, testartist), number = 1000)
    print("Hashsökning tog", round(hashtid, 4) , "sekunder")

"""
Funkade inte bra att söka på artistnamn när man kollar på sista namnet. problemet ligger i att när man har 
olika antal element så så blir sista namnet olika och då kan ett namn dyka upp tidigare. vilket får en tro att m an gjort fel
men om man söker på ett mer unikt namn som sång namn så får man inte det problemet. linjär sökningen stämmer då för 250000
element är tiden av 1000000 elements delat på 4. hash  är super snabbt och bin tar typ lika lång tid då log2 N.

Binärsökning går också ungefär lika snabbt varjegång men det går mycket snabbare än linjärt.Medan Hashning gå sjut snabbt
vilket är förväntat. Hashingn fungerear så att du skickar in ett ord osm omvnandlas till en nyckel som sedan dricekt öppnar
en dör.

Antal element = 250000
Linjärsökningen tog 26.1069 sekunder
binärsökningen tog 0.0071 sekunder
Hashsökning tog 0.0003 sekunder
Antal element = 500000
Linjärsökningen tog 54.4843 sekunder
binärsökningen tog 0.0078 sekunder
Hashsökning tog 0.0003 sekunder
Antal element = 1000000
Linjärsökningen tog 106.086 sekunder
binärsökningen tog 0.0082 sekunder
Hashsökning tog 0.0003 sekunder
"""


def main2(n):
    fil = "unique_tracks.txt"
    list = readfile(fil)

    print("Antal element =", n)
    list = list[:n]

    urvalstid = timeit.timeit(stmt=lambda: urvalssortera(list), number=1)
    print("Urvalssortering tog", round(urvalstid, 4), "sekunder")

    mergetid = timeit.timeit(stmt=lambda: mergesort(list), number=1)
    print("Mergesortering tog", round(mergetid, 4), "sekunder\n")



"""
Antal element = 1000
Urvalssortering tog 0.1862 sekunder
Mergesortering tog 0.0057 sekunder

Antal element = 10000
Urvalssortering tog 23.9577 sekunder
Mergesortering tog 0.127 sekunder

Antal element = 100000
Urvalssortering tog 2693.1477 sekunder  Ca 44,8 min
Mergesortering tog 1.0936 sekunder

Antal element = 1000000
Urvalssortering beräknat att ta ca 74,8 h 
Mergesortering tog 19.0136 sekunder

Merge sorteting splittar allting tills de är listor av ett och sedan jömför de varandra två och två osv. Det resultatet 
är förväntat. Medan Urvalsortering tar sjukt lång tid för större listor då den går igenom hela listan ett flertal gånger.
Urvalssortering för 1000000 är beräknad till 74,8 h och simulerades inte.
"""

import math
def Cot(x):
    return 1/(math.tan(math.radians(x)))




def Ackermann(Theta):
    """Added method that replaces the starting method of steering for Audi A6"""
    Wheelbase = 2.760
    Wheeltrack = 1.627
    BackWhidht = 1.874
    """Calculate the other wheelsangle we use cot*theta - cot*phi = Backwidth /Wheelbase """
    Phi = math.degrees(math.atan(1/((BackWhidht / Wheelbase) + Cot(Theta))))
    MeanAngle = (Phi + Theta) / 2
    """Radius of the inner front wheel"""
    R_if = ((Wheelbase / math.sin(Phi)) + (Wheeltrack - BackWhidht) / 2)
    """Radius of the outer front wheel"""
    R_of = ((Wheelbase / math.sin(Theta)) - (Wheeltrack - BackWhidht) / 2)
    """Mean radius of the front wheels"""
    R_MFW = (R_if + R_of) / 2
    return MeanAngle
K=10%5
print(K)
if K != 0:
    print("s")


