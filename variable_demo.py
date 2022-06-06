"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""

MusteriAdi = "İsacan"
MusteriSoyadi = "Donmez"
#MusteriAdSoyad = "İsacan" + " " + "Donmez"
MusteriAdSoyad = MusteriAdi + " " + MusteriSoyadi

MusteriCinsiyet = "Erkek"

musteriDogumYili = 1995
musteriYasi = 2023 - musteriDogumYili


print(MusteriAdSoyad)

#####################################


"""
    Siparişlerin Toplamı isteniyor,

    sipariş 1 => 110    TL
    sipariş 2 => 1100.5 TL
    sipariş 3 => 356.95 TL
"""

#print(110 + 1100.5 + 356.95)

order1 = 110
order2 = 1100.5
order3 = 356.95

#print(order1 + order2 + order3)

total = order1 + order2 + order3

print(total)



