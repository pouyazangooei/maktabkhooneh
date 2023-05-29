import random
javab = random.randint(1,99)
hads = int(input('guess something? '))
while hads != javab:
    if hads > javab:
        print('kochiktare')
    else:
        print('bozorgtare')
    hads = int(input('another guess? '))
print('you did it little bastard!')