from bintreeFile import Bintree
def sve():
    svenska = Bintree()                                 #given kod för att kolla om ens kod funkar
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = " ")
            else:
                svenska.put(ordet)             # in i sökträdet
    print("\n")
    return svenska

def eng(svenska):
    engelska = Bintree()                        # Utnyttjar samma grund kod som tidigare uppgift
    with open("engelska.txt", "r", encoding="utf-8") as engelskfil:
        for rad in engelskfil:
            rad = rad.strip()                   #tar bort radbrytningar (\n)
            ordet = rad.split(" ")              #splittar allt med mellanslag mellan
            for ord in ordet:                   #tar ut ett ord i taget
                if ord in svenska:              #kollan om ordet finns i svenska
                    if ord not in engelska:     #kollar om ordet inte finns i engelska
                        print(ord, end=" ")     #printar ordet om det finns i båda
                        engelska.put(ord)       #applicerar sedan om det finns
                    else:
                        pass
                else:
                    engelska.put(ord)           # om inte i svenska läggs det till i engelska
    print("\n")
sprak = sve()
eng(sprak)
