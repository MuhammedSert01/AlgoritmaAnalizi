import math
def enKucukBul(liste):
    enKucuk=liste[0]
    for i in liste:
        if enKucuk > i:
            enKucuk = i
    return enKucuk

def enBuyukBul(liste):
    enBuyuk=liste[0]
    for i in liste:
        if enBuyuk < i:
            enBuyuk = i
    return enBuyuk

def ortalamaBul(liste):
    toplam = 0
    for i in liste:
        toplam += int(i)
    return toplam/len(liste)

def varyansHesapla(liste, ort):
    kare = 0
    for i in liste:
        kare += pow((ort-int(i)),2)
    return kare

def normalDagilim(li, ort):
    normal=[]
    varyans = varyansHesapla(li, ort)
    average = ortalama
    for i in li:
        normal.append(1/varyans*math.sqrt(2*math.pi)*
                      pow(math.e, (-1)*(pow(int(i)-average, 2)/(2*pow(varyans,2)))))
    return normal
        
liste=[2,3,5,13,18,22]

enk=enKucukBul(liste)
print("en kucuk: ",enk)
enb=enBuyukBul(liste)
print("en buyuk: ",enb)
ortalama = ortalamaBul(liste)
print("ortalama: ",ortalama)
varyans= varyansHesapla(liste, ortalama)
print("varyans: ",varyans)
std=pow(varyans,1/2)
print("standart sapma: ",std)
normalDagilim= normalDagilim(liste, ortalama)
print("normal dagilim: ",normalDagilim)
