from molgrafik import *

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

rutan = Ruta()
rutan.atom = "C"
mol = Ruta(atom = "Cl", num = 2)
rutan.next = mol
mg = Molgrafik()
mg.show(rutan)
        
