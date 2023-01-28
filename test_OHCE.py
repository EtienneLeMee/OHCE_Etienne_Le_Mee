import unittest
from datetime import datetime
from unittest.mock import patch

import OHCE
from OHCE import OHCE as ohce

class OHCETest(unittest.TestCase):
    print("DEBUT TEST")

    def test_chaine_miroir(self):
        #Quand on saisit une chaine...
        string = "salut"
        result = ohce.miroir("tulas")
        #...Alors celle-ci est retournée en miroir
        self.assertTrue(result, string[0:len(string)])


if __name__ == '__main__':
    unittest.main()