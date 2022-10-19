from Trolleritrick import *

if __name__ == "__main__":
    stack, tomt = Kortlek()
    if tomt == False:
        print(Trick(stack))
    else:
        print("Leken är tom så vi kan inte trolla")
else:
    print("rip")

""" rätt ordning 7 1 12 2 8 3 11 4 9 5 13 6 10 """