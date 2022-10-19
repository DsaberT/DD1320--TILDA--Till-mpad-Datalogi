from yikes import *
from pokoclass import *

def pokemonHash():
    table = Hashtable(20000)
    with open("pokemon.csv", "r") as pokofile:
        for row in pokofile:
            info=row.split(",")
            pokodjur = Pokemon( info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10], info[11], info[12] )
            table.store( info[1], pokodjur )
    print(table.search("Pikachu").name)
    try:
        print(table.search("Diamond"))
    except KeyError:
        print("Ej funnen")
    print(table.search("Dialga").attack)
pokemonHash()