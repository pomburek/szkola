# Bitwa pod Wiedniem

liczba_choragwi = int(input())
choragwie = input().split()

def szyfr(numer):
    return sum(map(int, numer)), int(numer)

choragwie.sort(key=szyfr, reverse=True)

print(" ".join(choragwie))