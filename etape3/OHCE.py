class OHCE:

    def miroir(string):
        return string[::-1]

    def bien_dit(self):
        return "Bien dit !"

    def bien_dit_langue(self,langue):
        if langue=="fr":
            return "Bien dit !"
        elif langue=="en":
            return "Well done !"

    def au_revoir_langue(self,langue):
        if langue=="fr":
            return "Au revoir !"
        elif langue=="en":
            return "Bye !"

    def bonjour_langue_heure(self,langue,heure):
        if langue=="fr":
            if heure <= "12:00:00":
                return "Bonjour"
            elif heure <= "18:00:00":
                return "Bon apres-midi"
            elif heure <= "21:00:00":
                return "Bonsoir"
            else:
                return "Bonne soirée"
        elif langue=="en":
            if heure <= "12:00:00":
                return "Hello"
            elif heure <= "18:00:00":
                return "Good afternoon"
            elif heure <= "21:00:00":
                return "Good evening"
            else:
                return "Good night"

    def palindrome_langue_periode(string,langue,heure):
        ohce = OHCE()
        return OHCE.bonjour_langue_heure(ohce,langue,heure) \
            + OHCE.miroir(string) \
            + OHCE.bien_dit_langue(ohce,langue) \
            + OHCE.au_revoir_langue(ohce,langue)