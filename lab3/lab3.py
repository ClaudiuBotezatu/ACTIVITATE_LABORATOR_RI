import os
import random

# Functie hash pentru siruri (din lab 2)
def hash_sir(sir, r=31, n=10007):
    cod = 0
    for c in sir:
        cod = (r * cod + ord(c)) % n
    return cod

# Clasa pentru nodurile arborelui B+
class Nod:
    def __init__(self, e_frunza=False):
        self.e_frunza = e_frunza
        self.chei = []  # cheile hash
        self.valori = []  # pentru frunze
        self.copii = []  # pentru noduri interne
        self.urm = None  # legatura la urmatoarea frunza

# Clasa pentru arborele B+
class ArboreB:
    def __init__(self, t=2):  
        self.radacina = Nod(e_frunza=True)
        self.t = t

    def adauga(self, cheie, val):
        rad = self.radacina
        if len(rad.chei) == self.t:  
            nou_rad = Nod()
            self.radacina = nou_rad
            nou_rad.copii.append(rad)
            self._div_nod(nou_rad, 0)
            self._adauga_neplin(nou_rad, cheie, val)
        else:
            self._adauga_neplin(rad, cheie, val)

    def _div_nod(self, parinte, idx):
        t = self.t
        copil = parinte.copii[idx]
        nou_nod = Nod(e_frunza=copil.e_frunza)
        
        
        nou_nod.chei = copil.chei[t//2:]
        if copil.e_frunza:
            nou_nod.valori = copil.valori[t//2:]
        else:
            nou_nod.copii = copil.copii[t//2:]
        
        copil.chei = copil.chei[:t//2]
        if copil.e_frunza:
            copil.valori = copil.valori[:t//2]
        else:
            copil.copii = copil.copii[:t//2]
        
        
        if copil.e_frunza:
            nou_nod.urm = copil.urm
            copil.urm = nou_nod
        
        
        parinte.chei.insert(idx, nou_nod.chei[0])
        parinte.copii.insert(idx + 1, nou_nod)

    def _adauga_neplin(self, nod, cheie, val):
        if nod.e_frunza:
           
            i = 0
            while i < len(nod.chei) and nod.chei[i] < cheie:
                i += 1
            if i < len(nod.chei) and nod.chei[i] == cheie:
                
                nod.valori[i].append(val)
            else:
                nod.chei.insert(i, cheie)
                nod.valori.insert(i, [val])
        else:
            
            i = 0
            while i < len(nod.chei) and cheie > nod.chei[i]:
                i += 1
            copil = nod.copii[i]
            if len(copil.chei) == self.t:
                self._div_nod(nod, i)
                if cheie > nod.chei[i]:
                    i += 1
            self._adauga_neplin(nod.copii[i], cheie, val)

    def cauta(self, cheie):
        return self._cauta(self.radacina, cheie)

    def _cauta(self, nod, cheie):
        if nod.e_frunza:
            for i, k in enumerate(nod.chei):
                if k == cheie:
                    return nod.valori[i] 
            return None
        else:
            i = 0
            while i < len(nod.chei) and cheie > nod.chei[i]:
                i += 1
            return self._cauta(nod.copii[i], cheie)

# Listare fisiere din director
def lista_fisiere(folder):
    fisiere = []
    for rad, dir, fis in os.walk(folder):
        dir[:] = [d for d in dir if d not in ['.', '..']] 
        for f in fis:
            cale = os.path.join(rad, f)
            fisiere.append((f, cale))
        for d in dir:
            cale = os.path.join(rad, d)
            fisiere.append((d, cale))
    return fisiere

# Testare
def main():
    folder = input("Dati calea folderului: ")
    arb = ArboreB(t=2)
    
    # Indexam fisierele
    fisiere = lista_fisiere(folder)
    for nume, cale in fisiere:
        cheie = hash_sir(nume)
        arb.adauga(cheie, (nume, cale))
        print(f"Adaugat: {nume} cu cheia {cheie}")
    
    # Cautare
    caut = input("Dati nume fisier/director: ")
    cheie = hash_sir(caut)
    rez = arb.cauta(cheie)
    if rez:
        print("Gasit:")
        for nume, cale in rez:
            print(f"  Nume: {nume}, Cale: {cale}")
    else:
        print("Nu s-a gasit.")

if __name__ == "__main__":
    main()