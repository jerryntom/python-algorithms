def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


first = int(input("Pierwsza liczba: "))
second = int(input("Druga liczba: "))
print(nwd(first, second))
