from ArrayQclass import *


def Kortlek():
    kort = ArrayQ()
    print("Hur vill du ha korten?")
    ordning = input()                           #Här skriver man in vilke ordning på korten man vill ha
    ordning = ordning.split(" ")
    for i in ordning:                           # de adderas in en efter en
        kort.enqueue(i)
    return kort, kort.isEmpty()

def Trick(kort):
    magitrick = []
    while int(len(kort._array)) != 0:
        kort.enqueue(kort.dequeue())
        x = kort.dequeue()
        magitrick.append(x)
    return magitrick



stack, tomt = Kortlek()
if tomt == False:
    print(Trick(stack))
else:
    print("Leken är tom så vi kan inte trolla")
