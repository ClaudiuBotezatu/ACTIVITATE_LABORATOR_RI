
mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
]


def page_rank():
    n = 11  
    q = 0.15  
    pr = [1/n] * n  
    e = [q/n] * n  
    
    
    grad = [sum(linie) for linie in mat]  
    
    while True:
               
        pr_nou = [0] * n
        suma_pr = 0
        for p in range(n):
            suma = 0
            for w in range(n):
                if mat[w][p] == 1 and grad[w] > 0:  
                    suma += pr[w] / grad[w]
            pr_nou[p] = (1 - q) * suma + e[p]
            suma_pr += pr_nou[p]
        
        
        c = 1 / suma_pr
        for p in range(n):
            pr_nou[p] *= c
        
        
        dif = max(abs(pr_nou[p] - pr[p]) for p in range(n))
        pr = pr_nou.copy()
        
        if dif < 0.0001:  
            break
    
    return pr


def main():
    scoruri = page_rank()
    print("Scoruri PageRank:")
    for i, scor in enumerate(scoruri, 1):
        print(f"Pagina {i}: {scor:.4f}")

if __name__ == "__main__":
    main()