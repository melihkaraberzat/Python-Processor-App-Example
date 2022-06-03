def idnumber(kimlikno):
    if not len(kimlikno)==11: # 11 haneli degilse
        return 'invalid'
    if not kimlikno.isdigit(): # sayilardan olusmuyorsa
        return 'invalid' 
    if int(kimlikno[0])== 0: # ilk hanesi 0 ise
        return 'invalid'
    basamak = [int(d) for d in str(kimlikno)] 
    if not sum(basamak[:10]) % 10 == basamak[10]:
        return 'invalid'
    if not (((7 * sum(basamak[:9][-1::-2])) - sum(basamak[:9][-2::-2])) % 10) == basamak[9]:
        return 'invalid'
    return 'valid'   

girdi_dosyasi = open('inputFile.txt','r')
okunan_satirlar=girdi_dosyasi.readlines()
for satir in okunan_satirlar :
    girdi_alanlari = satir.split(",")
    kimlikno = girdi_alanlari[3]
    hesaplamalar = (int(girdi_alanlari[4]) - int(girdi_alanlari[5]))* int(girdi_alanlari[6])
    kimlikno = girdi_alanlari[3]  
    yazilacakbilgiler= girdi_alanlari[0]+' ' +girdi_alanlari[1]+","+girdi_alanlari[2]+","+str(idnumber(kimlikno))+","+str(hesaplamalar)
    adsoyad = girdi_alanlari[0]+"-"+girdi_alanlari[1]
    with open (adsoyad+'.'+'txt', 'w') as f:
        f.write(yazilacakbilgiler)
