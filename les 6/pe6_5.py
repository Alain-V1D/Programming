def kwadraten_som(grondgetallen):
    som = 0;

    for x in grondgetallen:
        if(x > 0):
            som += x**2;

    return som;
print(kwadraten_som([4,5,3,-81]));