import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 's'
ZMAGA = 'W'
PORAZ = 'X'


class Vislice:
    def __init__(self):
        self.igre = {}
        self.max_id = 0

    def prost_id_igre(self):
        self.max_id += 1
        return self.max_id

    '''Druga možnost
    def prost_id_igre_drugace(self):
        n = max(self.igre.keys())
        return n + 1
    '''

    def nova_igra(self):
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra(bazen_besed)

        self.igre[nova_igra] = {sveza_igra, ZACETEK}

        return nov_id

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]

        novo_stanje = igra.ugibaj(crka)

        self.igre[id_igre] = (igra, novo_stanje)


    


class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka.upper() not in self.geslo.upper()]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka.upper() in self.geslo.upper()]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        return vse_crke and STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak()
    
    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()

    def pravilni_del_gesla(self):
        delni = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for crka in self.geslo:
            if crka.upper() in ugibanje:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


with open('vislice/besede.txt', 'r') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])

#testno_geslo = 'DEŽUJE'
#testne_crke = ['A', 'I', 'O', 'U', 'J', 'D', 'K']
#igra = Igra(testno_geslo, testne_crke)