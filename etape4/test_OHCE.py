import unittest
from datetime import datetime
from unittest.mock import patch
from datetime import datetime
import locale

import OHCE
from OHCE import OHCE as ohce
import os

class OHCETest(unittest.TestCase):
    print("DEBUT TEST")

    def test_langue_systeme(self):
        bonjour = "Bonjour"
        #Etant donné un utilisateur parlant une langue
        langue = locale.getdefaultlocale()[0][:2]
        #Et la période de la journée
        heure = "08:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_horloge(self):
        bonjour = "Bonjour"
        #Etant donné un utilisateur parlant une langue
        langue = locale.getdefaultlocale()[0][:2]
        #Et la période de la journée
        currentDateAndTime = datetime.now()
        heure = currentDateAndTime.strftime("%H:%M:%S")
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_recette_un(self):
        # Etant donné un utilisateur parlant une langue
        langue = "en"
        # Et la période de la journée
        heure = "19:00:00"
        # Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn("Good evening", ohce.palindrome_langue_periode(palindrome, langue, heure)[:len("Good evening")])
        self.assertIn("kayak", ohce.palindrome_langue_periode(palindrome, langue, heure))
        self.assertIn("Well done !", ohce.palindrome_langue_periode(palindrome, langue, heure))
        self.assertIn("Good evening, see you soon !", ohce.palindrome_langue_periode(palindrome, langue, heure)[len("Good evening, see you soon !"):])

    def test_recette_deux(self):
        # Etant donné un utilisateur parlant une langue
        langue = "fr"
        # Et la période de la journée
        heure = "08:00:00"
        # Quand on saisit une chaîne
        palindrome = "salut"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn("Bonjour", ohce.palindrome_langue_periode(palindrome, langue, heure)[:len("Bonjour")])
        self.assertIn("tulas", ohce.palindrome_langue_periode(palindrome, langue, heure))
        self.assertNotIn("Bien dit !", ohce.palindrome_langue_periode(palindrome, langue, heure))
        self.assertIn("Au revoir !", ohce.palindrome_langue_periode(palindrome, langue, heure)[len("Au revoir !"):])



if __name__ == '__main__':
    unittest.main()