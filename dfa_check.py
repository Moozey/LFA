input_file = open("input.txt", 'r')
nr_stari = int(input_file.readline())
stari = [int(x) for x in input_file.readline().split()]
nr_tranzitii = int(input_file.readline())
tranzitii = [[0 for _ in range(nr_stari)] for _ in range(nr_stari)]

for i in range(nr_tranzitii):
    tranzitie = input_file.readline().split()
    linie = int(tranzitie[0])
    coloana = int(tranzitie[1])
    tranzitii[linie][coloana] = tranzitie[2]

stare_initiala = int(input_file.readline())    
nr_stari_finale = int(input_file.readline())
stari_finale = [ int(x) for x in input_file.readline().split()]
nr_cuvinte = int(input_file.readline()) 
cuvinte = []
for i in range(nr_cuvinte):
    cuv = input_file.readline().replace('\n', '')
    cuvinte.append(cuv)

for cuv in cuvinte:
    stare_curenta = stare_initiala
    for litera in cuv:
        ok = False
        for i in stari:
            if tranzitii[stare_curenta][i] == litera:
                stare_curenta = i
                ok = True
                break
        if not ok:
            print ("Nu")
            break
    if ok:
        if stare_curenta in stari_finale:
            print("Da")
        else: 
            print("Nu")

