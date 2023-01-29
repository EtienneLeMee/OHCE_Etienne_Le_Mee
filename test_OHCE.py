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
        self.assertTrue("tulas", ohce.miroir(motSaisie))

    def test_palindrome(self):
        #Quand on saisie un palindrome
        palindrome = "kayak"
        #Alors celui-ci est renvoyé
        self.assertIn("kayak",ohce.palindrome(palindrome))
        #Bien dit est envoyé ensuite
        self.assertIn("Bien dit !",ohce.palindrome(palindrome))

    def test_bonjour(self):
        #Quand on saisit une chaine
        palindrome = "kayak"
        bonjour = "Bonjour"
        #Alors bonjour est renvoyé avant toute réponse
        self.assertIn(bonjour,ohce.palindrome(palindrome)[0:len(bonjour)])

    def test_aurevoir(self):
        palindrome = "kayak"
        aurevoir = "Au revoir !"
        # Alors bonjour est renvoyé avant toute réponse
        self.assertIn(aurevoir, ohce.palindrome(palindrome)[-len(aurevoir):])

    def test_biendit_fr(self):
        #Etant donné un utilisateur parlant une langue
        langue = "fr"
        #Quand un palindrome est saisit
        palindrome = "kayak"
        # Alors celui-ci est renvoyé
        self.assertIn("kayak", ohce.palindrome_langue(palindrome,langue))
        # Bien dit dans la langue est envoyé ensuite
        self.assertIn("Bien dit !", ohce.palindrome_langue(palindrome,langue))

    def test_biendit_en(self):
        #Etant donné un utilisateur parlant une langue
        langue = "en"
        #Quand un palindrome est saisit
        palindrome = "kayak"
        # Alors celui-ci est renvoyé
        self.assertIn("kayak", ohce.palindrome_langue(palindrome,langue))
        # Bien dit dans la langue est envoyé ensuite
        self.assertIn("Well done !", ohce.palindrome_langue(palindrome,langue))

    def test_bonjour_fr(self):
        #Etant donné un utilisateur parlant une langue
        langue = "fr"
        # Quand on saisit une chaine
        palindrome = "kayak"
        bonjour = "Bonjour"
        # Alors bonjour est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue(palindrome,langue)[0:len(bonjour)])

    def test_bonjour_en(self):
        #Etant donné un utilisateur parlant une langue
        langue = "en"
        # Quand on saisit une chaine
        palindrome = "kayak"
        bonjour = "Hello"
        # Alors bonjour est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue(palindrome,langue)[0:len(bonjour)])

    def test_aurevoir_fr(self):
        #Etant donné un utilisateur parlant une langue
        langue = "fr"
        palindrome = "kayak"
        aurevoir = "Au revoir !"
        # Alors bonjour est renvoyé avant toute réponse
        self.assertIn(aurevoir, ohce.palindrome_langue(palindrome,langue)[-len(aurevoir):])

    def test_aurevoir_en(self):
        #Etant donné un utilisateur parlant une langue
        langue = "en"
        palindrome = "kayak"
        aurevoir = "Bye !"
        # Alors bonjour est renvoyé avant toute réponse
        self.assertIn(aurevoir, ohce.palindrome_langue(palindrome,langue)[-len(aurevoir):])



if __name__ == '__main__':
    unittest.main()