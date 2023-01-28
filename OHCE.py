class OHCE:
    def miroir(string):
        return string[::-1]

    def palindrome(string):
        return OHCE.miroir(string) \
            + "Bien dit !"
