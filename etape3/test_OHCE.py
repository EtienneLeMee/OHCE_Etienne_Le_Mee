import unittest
from datetime import datetime
from unittest.mock import patch

import OHCE
from OHCE import OHCE as ohce

class OHCETest(unittest.TestCase):
    print("DEBUT TEST")

    def test_bonjour_am_fr(self):
        bonjour = "Bonjour"
        #Etant donné un utilisateur parlant une langue
        langue = "fr"
        #Et la période de la journée
        heure = "08:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_bonjour_pm_fr(self):
        bonjour = "Bon apres-midi"
        #Etant donné un utilisateur parlant une langue
        langue = "fr"
        #Et la période de la journée
        heure = "14:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_bonjour_soir_fr(self):
        bonjour = "Bonsoir"
        #Etant donné un utilisateur parlant une langue
        langue = "fr"
        #Et la période de la journée
        heure = "19:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_bonjour_nuit_fr(self):
        bonjour = "Bonne soirée"
        #Etant donné un utilisateur parlant une langue
        langue = "fr"
        #Et la période de la journée
        heure = "23:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_bonjour_am_en(self):
        bonjour = "Hello"
        #Etant donné un utilisateur parlant une langue
        langue = "en"
        #Et la période de la journée
        heure = "08:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_bonjour_pm_en(self):
        bonjour = "Good afternoon"
        #Etant donné un utilisateur parlant une langue
        langue = "en"
        #Et la période de la journée
        heure = "14:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_bonjour_soir_en(self):
        bonjour = "Good evening"
        #Etant donné un utilisateur parlant une langue
        langue = "en"
        #Et la période de la journée
        heure = "19:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])

    def test_bonjour_nuit_en(self):
        bonjour = "Good night"
        #Etant donné un utilisateur parlant une langue
        langue = "en"
        #Et la période de la journée
        heure = "23:00:00"
        #Quand on saisit une chaîne
        palindrome = "kayak"
        # Alors bonjour dans cette langue et à cette periode est renvoyé avant toute réponse
        self.assertIn(bonjour, ohce.palindrome_langue_periode(palindrome,langue,heure)[:len(bonjour)])


if __name__ == '__main__':
    unittest.main()