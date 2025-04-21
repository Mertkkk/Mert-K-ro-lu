# Kullanıcıdan sözcük alınır
kelime = input("Bir sözcük girin: ")

# Kullanıcıdan sayı alınır
sayi = int(input("Kaçıncı harfi değiştirmek istiyorsunuz? (0'dan başlayarak): "))

# Kullanıcıdan yeni harf alınır
yeni_harf = input("Yeni harfi girin: ")

# Harfi değiştirme işlemi
if 0 <= sayi < len(kelime):
    yeni_kelime = kelime[:sayi] + yeni_harf + kelime[sayi+1:]
    print("Çıktı:", yeni_kelime)
else:
    print("Hata: Sayı, kelimenin uzunluğunu aşmamalı.")
