def diviseurs(n):
    L = []
    for i in range(n+1):
        if i%n == 0:
            L.append(i)
    return L