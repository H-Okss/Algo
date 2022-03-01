def pgcd(a,b):
    r = a%b
    while b:
        a,b = b,a%b
    return a