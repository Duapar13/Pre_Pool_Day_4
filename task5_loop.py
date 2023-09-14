nombre = int(input("ecrit un nombre "))
for i in range(2, nombre // 2 + 1):
    multiples = [j for j in range(i, nombre, i) if j < nombre]
    multiples.sort(reverse=True)
    print(multiples)
