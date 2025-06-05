# Clasa pentru nodurile trie
class Nod:
    def __init__(self):
        self.link = [None] * 27  
        self.e_final = False  


class Trie:
    def __init__(self):
        self.rad = Nod()

    def adauga(self, cuv):
        p = self.rad
        for c in cuv + '{':  
            idx = ord(c) - ord('a') if c != '{' else 26  
            if not p.link[idx]:  
                p.link[idx] = Nod()
            p = p.link[idx]
        p.e_final = True  

    def cauta(self, cuv):
        p = self.rad
        for c in cuv + '{':
            idx = ord(c) - ord('a') if c != '{' else 26
            if not p.link[idx]:
                return False
            p = p.link[idx]
        return p.e_final


def citeste_stopwords(fisier):
    try:
        with open(fisier, 'r') as f:
            return [linie.strip().lower() for linie in f if linie.strip()]
    except FileNotFoundError:
        print("Fisierul cu stopwords nu exista!")
        return []

def numara_stopwords(trie, text):
    cuvinte = text.lower().split()
    contor = 0
    for cuv in cuvinte:
        if trie.cauta(cuv):
            contor += 1
    return contor


def main():
    
    stopwords_fisier = "stopwords.txt"  
    trie = Trie()
    
    # Incarcam stopwords
    stopwords = citeste_stopwords(stopwords_fisier)
    if not stopwords:
        print("Nu s-au gasit stopwords. Folosim o lista mica.")
        stopwords = ["the", "is", "and", "to", "in"]  # exemplu
    for cuv in stopwords:
        trie.adauga(cuv)
    print(f"Adaugat {len(stopwords)} stopwords in trie.")

    #Text_test
    text = """
    This is a sample text to test the trie structure.
    We will count the stopwords in this text and see how it works.
    """
    
    
    nr_stopwords = numara_stopwords(trie, text)
    print(f"Numar stopwords gasite: {nr_stopwords}")

   
    test_cuv = input("Dati un cuvant pentru cautare: ").lower()
    if trie.cauta(test_cuv):
        print(f"Cuvantul '{test_cuv}' e in trie.")
    else:
        print(f"Cuvantul '{test_cuv}' nu e in trie.")

if __name__ == "__main__":
    main()