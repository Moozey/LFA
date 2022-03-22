input_file = open("input.txt", 'r')
nr_stari = int(input_file.readline())
stari = [int(x) for x in input_file.readline().split()]
nr_tranzitii = int(input_file.readline())
tranzitii = [[[] for _ in range(nr_stari)] for _ in range(nr_stari)]

for i in range(nr_tranzitii):
    tranzitie = input_file.readline().strip('\n')
    v=tranzitie.split()
    linie = int(v[0])
    coloana = int(v[1])
    tranzitii[linie][coloana].append(v[2])


stare_initiala = int(input_file.readline())    
nr_stari_finale = int(input_file.readline())
stari_finale = [ int(x) for x in input_file.readline().split()]
nr_cuvinte = int(input_file.readline()) 
cuvinte = []
for i in range(nr_cuvinte):
    cuv = input_file.readline().replace('\n', '')
    cuvinte.append(cuv)



def parcurg(stare_curenta, cuvant):         #functie recursiva parcurgere in adancime
    global ok
    copie = cuvant
    for i in range(nr_stari):
        if cuvant[0] in tranzitii[stare_curenta][i]:
            cuvant=cuvant[1:] #sterg primul caracter
            if len(cuvant)==0:
                if i in stari_finale:
                    ok=1
                return
            #print(x,i)
            #print(cuv)
            parcurg(i, cuvant)
            cuvant = copie


for cuv in cuvinte:
    if cuv =='' and stare_initiala in stari_finale: #tratez cazul in care avem cuvantul vid
        print("cuvantul dat este acceptat")
    else:
        ok = 0
        parcurg(stare_initiala, cuv)
        if ok==0:
            print("cuvantul dat nu este acceptat")
        else:
            print("cuvantul dat este acceptat")