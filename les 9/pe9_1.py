list = []
while True:
    getal = int(input('geef een getal: '))
    list.append(getal)
    if getal == 0:
        a = len(list) - 1
        b = sum(list)
        print('Er zijn ' + str(a) + ' getallen ingevoerd, De som daarvan is ' + str(b))
        break
    elif getal:
        continue