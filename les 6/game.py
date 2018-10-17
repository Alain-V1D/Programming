import random
aantalKolommen = 3
aantalRijen = 3

def setupGameBoard(kolommen, rijen):
    'maakt een tabel aan met daarin een enkele bom'

    #Maak een leeg board
    gameboard = []
    rij = []
    for x in range (0, rijen):
        for y in range (0, kolommen):
            rij.append('.')
        gameboard.append(rij)
        rij = []

    #Plaats de bom
    x = random.randrange(0, kolommen)
    y = random.randrange(0, rijen)
    gameboard[y][x] = 'B'
    return gameboard

def vraagGebruikerOmEenPositie():
    x = int(input('Geef een positie x:'))-1
    y = int(input('Geef een positie y:'))-1
    return x, y

def bepaalOfErEenBomLigt(gameboard, x, y):
    result = gameboard[y][x] == 'B'
    gameboard[y][x] = 'x'
    return result

def toonGameBoard(gameboard,beurt):
    for rij in range(len(gameboard)):
        print(gameboard[rij])
    print('Dit was je '+str(beurt)+'beurt')



gameboard = setupGameBoard(aantalKolommen, aantalRijen)

gameOver = False
beurt = 0

while not gameOver:
    beurt += 1
    x, y = vraagGebruikerOmEenPositie()
    gameOver = bepaalOfErEenBomLigt(gameboard, x, y)
    toonGameBoard(gameboard, beurt)

