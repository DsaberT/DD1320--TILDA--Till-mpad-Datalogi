from songclass import *

def linsok(allanamn,sist):      # O = N
    for element in allanamn:
        if element.songnamn == sist:
            return sist


def sortlista(allanamn):
    tomlista = []
    for element in allanamn:
        tomlista.append(element.songnamn)
    tomlista.sort()
    return tomlista


def binarsok(sortnamn, sist):   # O = log2 * N
    if len(sortnamn) == 0:
        pass
    else:
        mitten = len(sortnamn)//2
        if sortnamn[mitten] == sist:
            return sist
        else:
            if sist < sortnamn[mitten]:
                binarsok(sortnamn[:mitten], sist)
            else:
                binarsok(sortnamn[mitten+1:], sist)
    return sist


def binsearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

def Hashdict(list):
    hdict = {}
    for element in list:
        hdict[element.songnamn] = element
    return hdict

def Hashsok(hdict, sist):
    if sist == hdict[sist].songnamn:
        return sist


def urvalssortera(data): #O N^2
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]

def mergesort(data): #O n * log n
    if len(data) > 1:
        mitten = len(data)//2
        vensterHalva = data[:mitten]
        hogerHalva = data[mitten:]

        print(vensterHalva, "VH")
        print(hogerHalva, "HH")
        mergesort(vensterHalva)
        mergesort(hogerHalva)
        print(vensterHalva, "VH")
        print(hogerHalva, "HH")

        i, j, k = 0, 0, 0

        while i < len(vensterHalva) and j < len(hogerHalva):
            if vensterHalva[i] < hogerHalva[j]:
                data[k] = vensterHalva[i]
                print(data)
                i = i + 1
            else:
                data[k] = hogerHalva[j]
                print(data)
                j = j + 1
            k = k + 1

        while i < len(vensterHalva):
            data[k] = vensterHalva[i]
            print(data)
            i = i + 1
            k = k + 1

        while j < len(hogerHalva):
            data[k] = hogerHalva[j]
            print(data)
            j = j + 1
            k = k + 1