class OHCE:

    def miroir(string):
        return string[::-1]

    def bien_dit(self):
        return "Bien dit !"
    def bonjour(self):
        return "Bonjour"

    def au_revoir(self):
        return "Au revoir !"
    def palindrome(string):
        ohce = OHCE()
        return OHCE.bonjour(ohce) \
            + OHCE.miroir(string) \
            + OHCE.bien_dit(ohce) \
            + OHCE.au_revoir(ohce)

    def bien_dit_langue(self,langue):
        if langue=="fr":
            return "Bien dit !"
        elif langue=="en":
            return "Well done !"
    def palindrome_langue(string,langue):
        ohce = OHCE()
        return OHCE.bonjour(ohce) \
            + OHCE.miroir(string) \
            + OHCE.bien_dit_langue(ohce,langue) \
            + OHCE.au_revoir(ohce)