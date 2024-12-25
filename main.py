# Kullanıcıdan yaş ve not bilgilerini alıyoruz
alter = int(input("19 "))
note = float(input("Adayın notunu girin: "))

# Şartları kontrol ediyoruz
if alter >= 20 and alter <= 50 and note > 80:
    print("einstellen")  # Aday uygun, işe al
else:
    print("ablehnen")  # Aday uygun değil, reddedilir