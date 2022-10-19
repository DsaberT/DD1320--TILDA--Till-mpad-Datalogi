import unittest
from syntax import *


class SyntaxTest(unittest.TestCase):

    def teststorbokstav(self):
        self.assertEqual(StorBokstav("A"), True)
        self.assertEqual(StorBokstav("a"), False)

    def testlitenbokstav(self):
        self.assertEqual(LitenBokstav("B"), False)
        self.assertEqual(LitenBokstav("b"), True)

    def testNummer(self):
        self.assertEqual(Nummer("A"), "A är ingen siffra och innehåller andra tecken")
        self.assertEqual(Nummer("3"), True)
        self.assertEqual(Nummer("1"), str(1) + " är mindre än 2")

    def testAtom(self):
        self.assertEqual(Atom("Ag"), True)
        self.assertEqual(Atom("gA"), "g Är inte en Storbokstav och A Är inte en litenbokstav")
        self.assertEqual(Atom("g"), "g Är inte en stor bokstav")
        self.assertEqual((Atom("Agg")), "Atom kan inte vara 3 Lång.")

    def testMolekyl(self):
        self.assertEqual(Molekyl("A"), True)
        self.assertEqual(Molekyl("C5"), True)
        self.assertEqual(Molekyl("aB"), "a Är inte en stor bokstav")
        self.assertEqual(Molekyl("Av0"), "0 är mindre än 2")
        self.assertEqual(Molekyl("3C"), "k")


unittest.main()
