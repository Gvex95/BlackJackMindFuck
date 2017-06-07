import sys
import random


izracunato = [None] * 52
spil = [1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,]

def IzracunajMaxPara(i):
    if izracunato[i] == -1: #taj slucaj nije obradjen
        izbor = [0]
        for h in range (4+i,52):
            tmp = IshodRunde(i,h)
            if (tmp!=-4):
                #nema greske, il sam izgubio,nereseno,ili pobedio
                izbor.append(tmp + IzracunajMaxPara(h)) #posto nema greska, a proslo je h karata, apenduj rez i izracunaj opet od h-te karte 
        izracunato[i] = max(izbor)
    return izracunato[i]

def IshodRunde(i,h):
    igrac = 0
    delilac = 0
    #ako delimo neparan broj karti, npr delimo do 7 do 12 karte,dele se od 7 do 11, a zadnju kartu gledamo posebno
    #while deli 4 karte koje i igrac i delilac moraju da uzmu
    while(i<(h-(h-i)%2)):
        if (spil[i] == 1 and igrac <=10):
            igrac+=11
        else:
            igrac+=spil[i]
        if(spil[i+1] == 1 and delilac<=10):
            delilac+=11
        else:
            delilac+=spil[i+1]

        i+=2 #jer prvo uzima igrac pa delilac pa opet igrac pa opet delilac

    #nakon podeljene 4 karte
    if ((h-i)%2 != 0):
        if (spil[h-1] == 1 and igrac<=10):
            igrac+=11
        else:
            if(igrac + spil[h-1]<=21):
                igrac += spil[h-1]
            #igrac  ne vuce jer ce preci 21, znaci red je na dilera
            else:
                if (spil[h-1] == 1 and delilac <=10):
                    delilac+=11
                else:
                    if(delilac>igrac):
                        return -4
                    else:
                        delilac+= spil[h-1]

    if (delilac<17):
        return -4
    if (igrac>21):
        return -1
    if (delilac>21):
        return 1
    if (igrac>delilac):
        return 1
    if (igrac == delilac):
        return 0
    if (igrac < delilac):
        return -1


for i in range(0,10):
    random.shuffle(spil)
    print("SPIL: ",spil)

    for i in range(0,52):
        izracunato[i] = -1

    print("Maksimalno para za ceo dek karata: ")
    print(IzracunajMaxPara(0), "$")
    
