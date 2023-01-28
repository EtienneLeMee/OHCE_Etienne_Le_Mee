class OHCE:

    def miroir(string):
        return string[::-1]

    def bien_dit(self):
        return "Bien dit !"
    def bonjour(self):
        return "Bonjour"
    def palindrome(string):
        ohce = OHCE()
        return OHCE.bonjour(ohce) \
            + OHCE.miroir(string) \
            + OHCE.bien_dit(ohce)
