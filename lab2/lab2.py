import random
import string
import time


def hash_sir(sir, r=31, n=10007):
    cod = 0
    for c in sir:
        cod = (r * cod + ord(c)) % n
    return cod


def hash_numar(num, n=10007):
    return num % n


class TabelaHash:
    def __init__(self, n=10007):
        self.n = n
        self.tab = [[] for _ in range(n)]  
        self.nr_coliziuni = 0  # contor coliziuni

    def adauga(self, cheie, val):
        idx = cheie % self.n
        if self.tab[idx]:  # daca exista deja ceva, e coliziune
            self.nr_coliziuni += 1
        self.tab[idx].append(val)

    def cauta(self, cheie, val):
        idx = cheie % self.n
        for v in self.tab[idx]:
            if v == val:
                return True
        return False

# Generare date random
def gen_numere(n=10000):
    return [random.randint(1, 100000) for _ in range(n)]

def gen_siruri(n=10000, lung=10):
    return [''.join(random.choices(string.ascii_lowercase, k=lung)) for _ in range(n)]

# Testare
def main():
   
    print("Tabela pentru numere")
    tab_num = TabelaHash(n=10007)
    numere = gen_numere(10000)
    
    # Adaugare
    start = time.time()
    for x in numere:
        k = hash_numar(x)
        tab_num.adauga(k, x)
    timp_adaugare = time.time() - start
    print(f"Timp adaugare: {timp_adaugare:.4f} secunde")
    print(f"Coliziuni: {tab_num.nr_coliziuni}")

    # Cautare
    nr_cautari = 1000
    vals_cautare = random.sample(numere, nr_cautari)
    coliziuni_cautare = 0
    start = time.time()
    for x in vals_cautare:
        k = hash_numar(x)
        if len(tab_num.tab[k % tab_num.n]) > 1:
            coliziuni_cautare += 1
        tab_num.cauta(k, x)
    timp_cautare = time.time() - start
    print(f"Timp cautare ({nr_cautari} valori): {timp_cautare:.4f} secunde")
    print(f"Cautari cu coliziuni: {coliziuni_cautare}")

    
    print("\nTabela pentru siruri")
    tab_sir = TabelaHash(n=10007)
    siruri = gen_siruri(10000)
    
   
    start = time.time()
    for s in siruri:
        k = hash_sir(s)
        tab_sir.adauga(k, s)
    timp_adaugare = time.time() - start
    print(f"Timp adaugare: {timp_adaugare:.4f} secunde")
    print(f"Coliziuni: {tab_sir.nr_coliziuni}")

    
    vals_cautare = random.sample(siruri, nr_cautari)
    coliziuni_cautare = 0
    start = time.time()
    for s in vals_cautare:
        k = hash_sir(s)
        if len(tab_sir.tab[k % tab_sir.n]) > 1:
            coliziuni_cautare += 1
        tab_sir.cauta(k, s)
    timp_cautare = time.time() - start
    print(f"Timp cautare ({nr_cautari} valori): {timp_cautare:.4f} secunde")
    print(f"Cautari cu coliziuni: {coliziuni_cautare}")

if __name__ == "__main__":
    main()