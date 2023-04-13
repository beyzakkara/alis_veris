import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


fiyat = {'Ekmek': 1.75, 'Sut': 4.0, 'Kola': 8.0, 'Su': 1.5}

depo =	{
  'Ekmek': 3,
  'Sut': 2,
  'Kola': 2,
  'Su': 2
}

alisveris_sepeti = []

genel_toplam = 0 
gecici_toplam= 0 # secilen urunu gecici olark hesaplamak icin tanımladık
bakiye = 20

def clear_console():
    os.system('clear')

def kalan_urun(key,adet):
    
    if(adet <= depo[key] & depo[key] >= 1):
        depo[key] -= adet
        return 1
    else:
        print(f'\n\n>>>>>>>>> *** HATA!: {key} icin yetersiz stok! *** <<<<<<<<<\n\n')
        return 0

def secili_urun_toplam(secim,adet):
    
    gecici_toplam= adet * fiyat[secim] # gecici_toplam fiyatı dogru hesaplamak icin adet miktarı kadar urun fiyatini carpip toplama ekledik
    for i in range(0, adet):
        alisveris_sepeti.append(secim) # burada adet miktarınca urunu 'alisveris_sepeti' dizisine append yani ekleme yaptik
    return gecici_toplam
    
    
    
# kullanıcıya urun seceneklerini sunup ardından secimler yaptırıyoruz

while True:
    
    clear_console()
    print('\n*****Online Alisveris Sistemine Hosgeldiniz!*****\n\n>>> Urun Alis-veris Menusu <<<\n\nUrun listemiz asagidadir seciminizi yapiniz\n\n1. Ekmek: 1.75 TL\n2. Sut: 4.00 TL\n3. Kola: 8.00 TL\n4. Su: 1.50 TL\n\n***Diger Islemler asagidadir***\n\n5. Sepet Kontrol ve Urun Silme\n9. Programdan Cikis')
    
    print('\n***  🛒  Sepette Bulunan Urunler:   🛒  ***\n', alisveris_sepeti) 
    print('\nToplam alisveris tutari: ', genel_toplam, ' TL')
    secim = int(input('\nHangi urunu almak istersiniz? Sepet kontrol icin (5): '))

    if secim == 1:
        try:
            adet = int(input('\nKac adet "Ekmek" istersiniz?: '))
            temp = "Ekmek"
            if(kalan_urun(temp,adet)==1):
                genel_toplam += secili_urun_toplam(temp,adet)
            temp = ""
            
        except:
            clear_console()
            print("\n***** HATA (try-except): 'Ekmek' adeti icin girdiginiz deger bir tam sayi degil! *****")

    
    elif secim == 2:
        try:
            adet = int(input('\nKac adet "Sut" istersiniz?: '))
            
            temp = "Sut"
            if(kalan_urun(temp,adet)==1):
                genel_toplam += secili_urun_toplam(temp,adet)
            temp = ""
            
        except:
            clear_console()
            print("\n***** HATA (try-except): 'Sut' adeti icin girdiginiz deger bir tam sayi degil! *****")

            
    elif secim == 3:
        
        try:
            adet = int(input('\nKac adet "Kola" istersiniz?: '))
            
            temp = "Kola"
            if(kalan_urun(temp,adet)==1):
                genel_toplam += secili_urun_toplam(temp,adet)
            temp = ""
            
        except:
            clear_console()
            print("\n***** HATA (try-except): 'Kola' adeti icin girdiginiz deger bir tam sayi degil! *****")


    elif secim == 4:
        try:
            adet = int(input('\nKac adet "Su" istersiniz?: '))
        
            temp = "Su"
            if(kalan_urun(temp,adet)==1):
                genel_toplam += secili_urun_toplam(temp,adet)
            temp = ""
            
        except:
            clear_console()
            print("\n***** HATA (try-except): 'Su' adeti icin girdiginiz deger bir tam sayi degil! *****")

    elif secim == 9:
            quit()
                    
    elif secim == 5:
            clear_console()
            print("\n*********************\n*\n* Urun Silme Menusu *\n*\n*********************")
        
        # *** SEPET KONTROL ve Ürün Silme islemleri ***
      
            while True:

                print('\n***  🛒  Sepette Bulunan Urunler:   🛒  ***\n', alisveris_sepeti)
                print('\nToplam alisveris tutari: ', genel_toplam, ' TL')
                print('\n1. Ekmek\n2. Sut\n3. Kola\n4. Su\n5. Silme Isleminden Cikis (Ana Menüye Dön)\n9. Programdan Cikis')
                    
                if not alisveris_sepeti: # eger 'alisveris_sepeti' dizisi ici bossa bir hata mesajı print ettik
                    clear_console()
                    print('\n*** HATA: Sepetinizde urun bulunmamaktadir! ***\n')
                        
    
                # silmek istedikleri urunu kullaniciya soruyoruz
                try:
                    print('\n***  🛒  Sepette Bulunan Urunler:   🛒  ***\n', alisveris_sepeti)
                    secim_silme = int(input('\nHangi urunu sepetten silmek istersiniz? Ana Menuye Don (5): '))
                except:
                    clear_console()
                    print("\n***** HATA (try-except): Urun silmek icin girdiginiz deger bir tam sayi degil!*****")
                        
                if secim_silme == 1:
                    clear_console()
                    alisveris_sepeti.remove('Ekmek')
                    depo['Ekmek'] += 1
                    genel_toplam -= 1.75
    
                elif secim_silme == 2:
                    clear_console()
                    alisveris_sepeti.remove('Sut')
                    depo['Sut'] += 1
                    genel_toplam -= 4.0
                        
                elif secim_silme == 3:
                    clear_console()
                    alisveris_sepeti.remove('Kola')
                    depo['Kola'] += 1
                    genel_toplam -= 8.0
                        
                elif secim_silme == 4:
                    clear_console()
                    alisveris_sepeti.remove('Su')
                    depo['Su'] += 1
                    genel_toplam -= 1.5
                       
                elif secim_silme == 5:
                    clear_console()
                    break
                        
                elif secim_silme == 9:
                    clear_console()
                    quit()

    print('\n***  🛒  Sepette Bulunan Urunler:   🛒  ***\n', alisveris_sepeti)
    print('\nToplam alisveris tutari: ', genel_toplam, ' TL')
  
    alisveris_devam_et = int(input('Baska bir urun almak ister misiniz? Evet (1) veya Hayir (0): '))
    if(alisveris_devam_et == 0):
        print('\n***Sepette Bulunan Urunler: ***\n', alisveris_sepeti)
        print('\nOdeyeceginiz Tutar: ', genel_toplam, ' TL')
        quit()
    else:
        continue
clear_console()
print('\nOdeyeceginiz Tutar: ', genel_toplam, ' TL')
