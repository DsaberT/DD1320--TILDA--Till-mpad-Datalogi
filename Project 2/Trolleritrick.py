from linkedQfile import *

def Kortlek():
    kort = LinkedQ()
    print("Hur vill du ha korten?")
    ordning = input()
    ordning = ordning.split(" ")
    for i in ordning:
        kort.enqueue(i)
    return kort, kort.isEmpty()

def Trick(kort):
    magitrick = []
    while not(kort.isEmpty()):
        kort.enqueue(kort.dequeue())
        x = kort.dequeue()
        magitrick.append(x)
    return magitrick
