import sys
from molgrafik import *
from vikter import *

class Syntaxfel(Exception):
    pass

atomlista = skapaAtomlista()
hashtabell = lagraHashtabell(atomlista)

class Node:
    def __init__(self, value, nextobject=None):
        self.value = value
        self.nextobject = nextobject

class LinkedQ:
    def __init__(self):
        self._first = None
        self._last = None

    def Queue(self):
        self._first = None
        self._last = None

    def enqueue(self, x):
        nynode = Node(x)
        if self._first == None:
            self._first = nynode
            self._last = nynode
        else:
            self._last.nextobject = nynode
            self._last = nynode

    def dequeue(self):
        topstack = self._first.value
        self._first = self._first.nextobject
        return topstack


    def isEmpty(self):
        if self._first == None:
            return True
        else:
            return False

    def peek(self):
        return self._first.value

def lanka(strang):
    q = LinkedQ()
    Mlist = list(strang)
    for i in range(len(Mlist)):
        q.enqueue(Mlist[i])
    if q.peek() == "#":
        return False
    q.enqueue("\n")
    return q

def readFormel(q):
    mol = readMolekyl(q)
    if not q.isEmpty():
        if q.peek() == (")"):
            mol = readMolekyl(q)
    return mol

def readMolekyl(q):
    mol = readGroup(q)
    if q.peek()== (")"):
        return mol
    elif q.peek() == ("\n"):
        return mol
    else:
        mol.next = readMolekyl(q)
        return mol


def readGroup(q):
    rutan = Ruta()
    if q.peek() == "(":
        q.dequeue()
        rutan.down = readMolekyl(q)
        if q.peek() == ")":
            q.dequeue()
            if sifferkoll(q.peek()) == True:
                rutan.num = readNum(q)
                return rutan
            raise Syntaxfel("Saknad siffra")
        if q.peek() == ("\n"):
            raise Syntaxfel("Saknad högerparentes")
    rutan.atom = readAtom(q)
    if not q.isEmpty():
       rutan.num = readNum(q)
    return rutan




def readAtom(q):
    if readLETTER(q) == True:
        atom = q.dequeue()
        if not q.isEmpty() and readletter(q):
            atom = atom + q.dequeue()
    elif readletter(q) == True:
        raise Syntaxfel("Saknad stor bokstav")
    else:
        raise Syntaxfel("Felaktig gruppstart")
    if atom in ['H',   'He',  'Li',  'Be',  'B',   'C',   'N',   'O',   'F',   'Ne', \
                'Na',  'Mg',  'Al',  'Si',  'P',   'S',   'Cl',  'Ar',  'K',   'Ca', \
                'Sc',  'Ti',  'V',   'Cr',  'Mn',  'Fe',  'Co',  'Ni',  'Cu',  'Zn', \
                'Ga',  'Ge',  'As',  'Se',  'Br',  'Kr',  'Rb',  'Sr',  'Y',   'Zr', \
                'Nb',  'Mo',  'Tc',  'Ru',  'Rh',  'Pd',  'Ag',  'Cd',  'In',  'Sn', \
                'Sb',  'Te',  'I',   'Xe',  'Cs',  'Ba',  'La',  'Ce',  'Pr',  'Nd', \
                'Pm',  'Sm',  'Eu',  'Gd',  'Tb',  'Dy',  'Ho',  'Er',  'Tm',  'Yb', \
                'Lu',  'Hf',  'Ta',  'W',   'Re',  'Os',  'Ir',  'Pt',  'Au',  'Hg', \
                'Tl',  'Pb',  'Bi',  'Po',  'At',  'Rn',  'Fr',  'Ra',  'Ac',  'Th', \
                'Pa',  'U',   'Np',  'Pu',  'Am',  'Cm',  'Bk',  'Cf',  'Es',  'Fm', \
                'Md',  'No',  'Lr',  'Rf',  'Db',  'Sg',  'Bh',  'Hs',  'Mt',  'Ds', \
                'Rg',  'Cn',  'Fl',  'Lv']:
        return atom
    else:
        raise Syntaxfel("Okänd atom")


def readLETTER(q):
    tecken = q.peek()
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if tecken in ABC:
        return True
    return False

def readletter(q):
    tecken = q.peek()
    abc = "abcdefghijklmnopqrstuvwxyz"
    if tecken in abc:
        return True
    return False

def readNum(q):
    if sifferkoll(q.peek()) == True:
        first = q.dequeue()
        if first == "0":
            raise Syntaxfel("För litet tal")
        if first == "1":
                if not sifferkoll(q.peek()):
                    raise Syntaxfel("För litet tal")
        while not q.isEmpty():
            if sifferkoll(q.peek()) == True:
                first = first + q.dequeue()
            else:
                return int(first)
    return 1

def sifferkoll(siffra):
    try:
        siffra = int(siffra)
        return True
    except ValueError:
        return False

def PrintQueue(q):
    strang = ""
    while not q.isEmpty():
        tecken = q.dequeue()
        if tecken != "\n":
            strang = strang + tecken
    return str(strang)

def Weight(ruta):
    if ruta != None:
        if ruta.down != None:
            massan = (ruta.num * Weight(ruta.down))
        else:
            massan = int(ruta.num) * hashtabell.search(ruta.atom).vikt
        return massan + Weight(ruta.next)
    return 0

def main(tex):
    while True:
        try:
            q = lanka(tex)
            if q == False:
                return False
            else:
                mol = readFormel(q)
                massan = Weight(mol)
                mg = Molgrafik()
                mg.show(mol)
                return("Massan för " + str (tex)+" är: " + str(massan) )
        except Syntaxfel as Fel:
            Strang = PrintQueue(q)
            if Strang == "":
                return str(Fel) + " vid radslutet"
            return str(Fel) + " vid radslutet " + str(Strang)


print(main("Si(C3(COOH)2)4(H2O)7"))
