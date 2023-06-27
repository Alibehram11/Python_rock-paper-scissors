import random
bilgisayar = 0
ben = 0

oyun = ["taş","kağıt","makas"]
print("Taş Kağıt Makas Oyununa Hoşgeldiniz Lütfe Bir Şey Seçin")
while True:
    soru = str(input("Taş Kğıt Makas:"))
    soru.lower()
    tahmin = random.choice(oyun)
    print("bilgisayar:",tahmin)
    print("siz:",soru)


    if soru  not in oyun:
        print("geçerli bir seçim yapmadınız")
        continue

    if soru == tahmin:
        print("barabere")
    
    elif (soru == "taş" and tahmin == "makas") or (soru == "makas" and tahmin == "kağıt") or (soru == "kağıt" and tahmin == "taş"):
        print("tebrikler kazandınız ")
        ben+=10
        print("benim",ben)
    else:
        print("kaybettiniz")
        bilgisayar+=10
        print("bilgisayar",bilgisayar)

    if 20 == ben or 20 == bilgisayar:
        print("puanınınız",ben)
        print("puanı",bilgisayar)
        break





