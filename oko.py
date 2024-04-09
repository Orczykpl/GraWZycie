# Gra w życie Johna Conwaya
import random, time, copy, os
import subprocess

subprocess.call('clear', shell=True)  # Dla systemów Unixowych

WIDTH = 10
HEIGHT = 10

# Utworzenie listy list przedstawiajacej komórki
nextCells = []
for x in range(WIDTH):
    column = [] # Utworzenie nowej kolumny
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Dodawanie komórki żywej
        else:
            column.append(' ') # Dodawanie komórki martwej
    nextCells.append(column) # nextCells to lista kolumn

licznik = 0
powtorki = 0
while True: # Pętla główna programu
    licznik += 1
    print('\n\n\n\n\n') # Oddzielanie poszczególnych kroków znakami nowego wiersza
    print(f"GRA W ŻYCIE! iterracja: {licznik}")
    currentCells = copy.deepcopy(nextCells)

    # Wyświetlanie currentCells na ekranie.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Wyświetlanie znaku # lub spacji.
        print() # Wyświetlanie znaku nowego wiersza na końcu danego wiersza komórek.

    # Obliczanie komórek w następnym kroku na podstawie komórek bierzącego kroku.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Pobranie współrzędnych komórek sąsiadujących z daną komórką.
            # '% WIDTH' gwarantuje, że wartość leftCoord zawsze będzie w przedziale od 0 do WIDTH -1.
            leftCord  = (x - 1) % WIDTH
            rightCord = (x + 1) % WIDTH
            aboveCord = (y - 1) % HEIGHT
            belowCord = (y + 1) % HEIGHT

            # Liczba sąsiadujących żywych komórek.
            numNeightbors = 0
            if currentCells[leftCord][aboveCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka w lewym górnym rogu jest żywa.
            if currentCells[aboveCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka na górze jest żywa.
            if currentCells[rightCord][aboveCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka w prawym górnym rogu jest żywa.
            if currentCells[leftCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka po lewej stronie jest żywa.
            if currentCells[rightCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka po prawej stronie jest żywa.
            if currentCells[leftCord][belowCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka w lewym dolnym rogu jest żywa.
            if currentCells[belowCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka na dole jest żywa.
            if currentCells[rightCord][belowCord] == '#':
                numNeightbors += 1 # Sąsiadująca komórka w prawym dolnym rogu jest żywa.

            # Określenie stanu komórki na podstawie regół gry w życie Johna Conwaya.
            if currentCells[x][y] == '#' and (numNeightbors == 2 or numNeightbors == 3):
                # Dwie lub trzy żywe komórki sąsiadujące oznaczają, że komórka pozostaje żywa.
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeightbors == 3:
                # Trzy żywe komórki sąsiadujące oznaczają, że komórka ożywa.
                nextCells[x][y] = '#'
            else:
                # Reszta komórek pozostaje martwa lub obumiera.
                nextCells[x][y] = ' '


    if currentCells == nextCells:
        break

    if licznik == 200:
        break

    time.sleep(0.2) # Dodanie sekundowej przerwy, aby zminimalizować migotanie
    subprocess.call('clear', shell=True)  # Dla systemów Unixowych
