menu = """"
                    ---------------------------
                    |       CARSHOP           |
                    ---------------------------
                    | 1.Arabaları listele     |
                    | 2.Araba satın al        |
                    | 3.Araba sat             |
                    | 4.Araba kirala          |
                    | 5.Çıkış                 |    
                    ---------------------------
"""
giris = """
----HOŞGELDİNİZ----
|1.Giriş          |
|2.Kayıt          |
|3.Çıkış          |
-------------------
"""
kullanıcı = {"1":{"ad":"Ahmet", "sifre": "1234"},"2":{"ad":"Salih", "sifre": "4321"},"3":{"ad":"Dila", "sifre": "1122"}}
araba = {"1": {"marka":"Hyundai", "model": "Accent blue","u_yili":"2012","plaka":"59LF887","fiyat":"670.000",'durum': 'Mevcut'},
         "2":{"marka":"Nissan", "model": "350z","u_yili":"2004","plaka":"17ZZ457","fiyat":"3.200.000",'durum': 'Mevcut'},
         "3":{"marka":"Mercedes", "model":"c200","u_yili":"2022","plaka":"34ZC542","fiyat":"4.050.000",'durum': 'Mevcut'} }

yanlishak = 3

kayıt = True
anamenu = False
print(giris)
while kayıt:
    sec = input("Bir işlem seçiniz:")
    if sec == "1":
        ıd = input("ID giriniz:")
        if ıd in kullanıcı:
            ad    = input("Adınızı giriniz:")    
            sifre = input("Sifre giriniz:")
            if ad == kullanıcı[ıd]["ad"] and sifre == kullanıcı[ıd]["sifre"]:
                    print("Başarıyla giriş yaptınız.")
                    kayıt = False
                    anamenu = True
                    print(menu)
            else:
                yanlishak -= 1
                print(f"Yanlış kullanıcı adı ya da şifre.Kalan hakkınız:{yanlishak}")
                if yanlishak == 0:
                    print("Hesabınız bloke olmuştur.")
                    kayıt = False     
        else:
            yanlishak -= 1
            print(f"ID yanlış.Kalan hakkınız:{yanlishak}")
            if yanlishak == 0:
                print("Hesabınız bloke olmuştur.")
                kayıt = False
    if sec == "2":
        yeni_id = input("İstediğiniz ID numarasını giriniz:")
        if yeni_id in kullanıcı:
            print("Zaten bu ID bulunmaktadır.")
        else:
            yeni_ad = input("İsminizi giriniz:")
            yeni_sifre = input("Şifrenizi giriniz:")  
            kullanıcı[yeni_id] = {"ad":yeni_ad,"sifre":yeni_sifre}
    if sec == "3":
        print("İyi günler.")
        kayıt = False        
while anamenu:
    sec2 = input("Bir işlem seçiniz:")
    if sec2 == "1":
        for a_id,bilgi in araba.items():
            print(f"ID: {a_id}  |Marka: {bilgi['marka']}   |Model: {bilgi['model']}  |Uretim Yili: {bilgi['u_yili']}   |Plaka: {bilgi['plaka']}   |Fiyat: {bilgi['fiyat']}   |Durum: {bilgi['durum']}")
    if sec2 == "2":
        secim = input("Bir araba seçiniz:")
        if secim in araba:
            if  araba[secim]['durum'] == 'Mevcut':
                araba[secim]['durum'] = "Satıldı"
                print(f"{araba[secim]['model']} hayırlı olsun.")
            else:
                print("Bu araba zaten satıldı.")
        else:
            print("Geçersiz ID.")
    if sec2 == "3":            
        yeni_id = input("Bir ID giriniz:")
        if yeni_id in araba:
            print("Bu ID zaten mevcut başka ID seçiniz")
        else:
            yeni_marka   =    input("Arabanızın markasını giriniz:")    
            yeni_model   =    input("Arabanızın modelini giriniz:")   
            yeni_uyıl    =    input("Arabanızın üretim yılını giriniz:")   
            yeni_plaka   =    input("Arabanızın plakasını giriniz:")
            yeni_fiyat   =    input("İstediğiniz fiyatını giriniz:")
            araba[yeni_id] = {
                'marka' :  yeni_marka,
                'model' :  yeni_model,
                'u_yili':  yeni_uyıl ,
                'plaka' :  yeni_plaka,
                'fiyat' :  yeni_fiyat,
                'durum' : "Mevcut"
            } 
            print(f"        Paranız:{yeni_fiyat}")            
    if sec2 == "4":
        secim = input("Bir araba seçiniz:")
        if secim in araba:
            if  araba[secim]['durum'] == 'Mevcut':
                araba[secim]['durum'] = "Kiralandi"
                print(f"{araba[secim]['model']} 1 aylık kiraladınız.")
            else:
                print("Bu araba zaten kiralandi.")
        else:
            print("Geçersiz ID.")     
    
    if sec2 == "5":
        print("İyi günler.")
        anamenu = False        