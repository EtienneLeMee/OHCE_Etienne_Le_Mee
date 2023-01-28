import unittest
from datetime import datetime
from unittest.mock import patch

import OHCE
from OHCE import OHCE as ohce

class OHCETest(unittest.TestCase):
    print("DEBUT TEST")

    def test_chaine_miroir(self):
        #Quand on saisit une chaine...
        motSaisie = "salut"
        #...Alors celle-ci est retournée en miroir
        self.assertTrue("tulas", motSaisie[0:len(motSaisie)])

    def test_palindrome(self):
        #Quand on saisie un palindrome
        palindrome = "kayak"
        #Alors celui-ci est renvoyé
        self.assertIn(ohce.palindrome(palindrome),"kayak")
        #Bien dit est envoyé ensuite
        self.assertIn(ohce.palindrome(palindrome),"Bien dit !")


if __name__ == '__main__':
    unittest.main()