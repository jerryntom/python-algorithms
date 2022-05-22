from time import sleep

def parzyste(a, b):
    if a % 2 == 0:
        pass
    else:
        a += 1
        print(a)
        a += 2

    i = a

    for i in range(a, b, 2):
        print(i)

    if i < b and b - i != 1:
        print(i + 2)


while True:
    try:
        start = int(input('Podaj poczatek przedzialu: '))
        end = int(input('Podaj koniec przedzialu: '))

        if start == end or start > end:
            raise ValueError

        break
    except Exception:
        print('Wprowadzono zle wartosci! Sprobuj ponownie!')
        sleep(1)
        print('\n')


print(start, end, '\n')
parzyste(start, end)
