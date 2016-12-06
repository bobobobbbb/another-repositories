def handle(letters):
    P = []; y = []; t = []; h = []; o = []; n = []; result = []
    for letter in letters:
        lit = {
            'P': P, 'y': y, 't': t,
            'h': h, 'o': o, 'n': n
        }.get(letter)
        if isinstance(lit, list): lit.append(letter)
    while (P or y or t or h or o or n):
        if P: result.append(P[0]); del P[0]
        if y: result.append(y[0]); del y[0]
        if t: result.append(t[0]); del t[0]
        if h: result.append(h[0]); del h[0]
        if o: result.append(o[0]); del o[0]
        if n: result.append(n[0]); del n[0]
    return "".join(result)
        
## main
if __name__ == "__main__":
    letters = input()
    print(handle(letters))
