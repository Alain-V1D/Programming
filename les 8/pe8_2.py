list = eval(input("Geef lijst met minimaal 10 strings: "))

list2 = []
for strings in list:
    if len(strings) == 4:
        list2.append(strings)

print('De nieuw gemmakt lijst met vier-letter strings is:')
print(list2)