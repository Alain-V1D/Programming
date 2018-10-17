def convert(temperatuurcelsius):
    fahrenheit = temperatuurcelsius * 1.8 + 32
    return fahrenheit


print(convert(25))


def table(n):
    for i in range(0, 80, 10):
        celsius = n + i
        print(celsius, end=' ')
        print(convert(celsius))

print(table(-30))

def convert(tempCelsius):
    res = ((tempCelsius*1.8)+32)
    return res

def table(vanafTemp, totTemp, gradenPerStap):
    print('(:5)   (:5)'.format("  F  ", "  C  "))
    for tempCelsius in range(vanafTemp, totTemp, gradenPerStap):
        tempFahrenheit = convert(tempCelsius)
        print('(:5)   (:5)'.format(tempFahrenheit, float(tempCelsius)))

print(table(-30, 50, 10))