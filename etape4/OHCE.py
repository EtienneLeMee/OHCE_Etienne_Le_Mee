import locale
from datetime import datetime


class OHCE:

    def miroir(string):
        return string[::-1]

    def bien_dit(self):
        return "Bien dit !"

    def bien_dit_langue(self, string, langue):
        if string[::-1] == string:
            if langue == "fr":
                return "Bien dit !"
            elif langue == "en":
                return "Well done !"
        else:
            return ""

    def bonjour_langue_heure(self, langue, heure):
        if langue == "fr":
            if heure <= "12:00:00":
                return "Bonjour"
            elif heure <= "18:00:00":
                return "Bon apres-midi"
            elif heure <= "21:00:00":
                return "Bonsoir"
            else:
                return "Bonne soirée"
        elif langue == "en":
            if heure <= "12:00:00":
                return "Hello"
            elif heure <= "18:00:00":
                return "Good afternoon"
            elif heure <= "21:00:00":
                return "Good evening"
            else:
                return "Good night"

    def aurevoir_langue_heure(self, langue, heure):
        if langue == "fr":
            if heure <= "12:00:00":
                return "Au revoir !"
            elif heure <= "18:00:00":
                return "Bon fin d'apres-midi !"
            elif heure <= "21:00:00":
                return "Bonne fin de soirée !"
            else:
                return "Bonne nuit !"
        else:  # Initial language is en
            if heure <= "12:00:00":
                return "Bye !"
            elif heure <= "18:00:00":
                return "Good afternoon, see you soon !"
            elif heure <= "21:00:00":
                return "Good evening, see you soon !"
            else:
                return "Good night, see you soon !"

    def saisie(self):
        return str(input("Saisissez votre mot : "))

    def palindrome_langue_periode(string, langue, heure):
        ohce = OHCE()
        print(OHCE.bonjour_langue_heure(ohce, langue, heure))
        if string == "":
            saisie = OHCE.saisie()
            print(OHCE.miroir(saisie))
            print(OHCE.bien_dit_langue(ohce, saisie, langue))
            print(OHCE.aurevoir_langue_heure(ohce, langue, heure))
            return OHCE.bonjour_langue_heure(ohce, langue, heure) \
                   + OHCE.miroir(saisie) \
                   + OHCE.bien_dit_langue(ohce, saisie, langue) \
                   + OHCE.aurevoir_langue_heure(ohce, langue, heure)
        else:
            print(OHCE.miroir(string))
            print(OHCE.bien_dit_langue(ohce, string, langue))
            print(OHCE.aurevoir_langue_heure(ohce, langue, heure))
            return OHCE.bonjour_langue_heure(ohce, langue, heure) \
                   + OHCE.miroir(string) \
                   + OHCE.bien_dit_langue(ohce, string, langue) \
                   + OHCE.aurevoir_langue_heure(ohce, langue, heure)


def main(self):
    sysLangue = locale.getdefaultlocale()[0][:2]
    currentDateAndTime = datetime.now()
    heure = currentDateAndTime.strftime("%H:%M:%S")
    self.palindrome_langue_periode("",sysLangue, heure)


if __name__ == '__main__':
    ohce = OHCE
    main(ohce)
