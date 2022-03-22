def AFN():
    f = open("input.txt")

    N = int(f.readline())
    Stari = [int(x) for x in f.readline().split()]
    M = int(f.readline())
    Tranzitii = []
    for i in range(0, M):
        linie = [x for x in f.readline().split()]
        linie[0] = int(linie[0])
        linie[1] = int(linie[1])
        Tranzitii.append(linie)

    S = int(f.readline())  # Stare initiala
    nrF = int(f.readline())  # Nr de stari finale
    StariFinale = [int(x) for x in f.readline().split()]

    nrCuv = int(f.readline())  # Nr cuvinte ce urmeaza a fi testate

    Cuvinte = [cuv[:len(cuv)-1] for cuv in f.readlines()]

    f.close()

    f = open("output.txt", "w")

    for Cuv in Cuvinte:
        StareCrt = set([S])
        for litera in Cuv:
            StareNoua = set()
            for Tranzitie in Tranzitii:
                for Stare in StareCrt:
                    if Stare == Tranzitie[0] and litera == Tranzitie[2]:
                        StareNoua.add(Tranzitie[1])
            StareCrt = StareNoua

        for Stare in StareCrt:
            if Stare in StariFinale:
                f.write(" DA" + "\n")
                break
        else:
            f.write(" NU" + "\n")
    f.close()

AFN()
