# class telefon:
#     def __init__(self,model):
#         self.model=model

#     def zaryadlash(self,foiz):
#         self.__foiz = foiz

#     def ishlatish(self,foiz):
#         self.__foiz -= foiz

#     def show(self):
#         return f"Model:{self.model},Foiz: {self.__foiz}"


# tel=telefon("Samsung S24")
# tel.zaryadlash(50)
# tel.ishlatish(20)
# print(tel.show())





# class hamyon:
#     def __init__(self,egasi,pul=0):
#         self.egasi=egasi
#         self.__pul=pul

#     def cash_in(self,som):
#         if som>0:
#             self.__pul+=som
#         else:
#             print("Noto'g'ri kiritildi")

#     def cash_out(self,som):
#         if som>0 and som<=self.__pul:
#             self.__pul-=som
#         else:
#             print("Noto'g'ri kiritildi")

#     def show(self):
#         return f"Egasi:{self.egasi},Pul: {self.__pul}"


# ham=hamyon("Aziz",100000)
# ham.cash_in(50000)
# ham.cash_out(20000)
# print(ham.show())










# class Qahramon:
#     def __init__(self, ism):
#         self.ism = ism              
#         self.__jon = 100            
#         self.__tirik = True         

#     def zarar_olish(self, zarar):
#         if self.__tirik:  
#             self.__jon -= zarar
#             if self.__jon <= 0:
#                 self.__jon = 0
#                 self.__tirik = False

#     def davolanish(self, miqdor):
#         if self.__tirik: 
#             self.__jon += miqdor
#             if self.__jon > 100:
#                 self.__jon = 100

#     def jon_korish(self):
#         return self.__jon

#     def tirikmi(self):
#         return self.__tirik


# q = Qahramon("Arslon")

# for _ in range(3):
#     q.zarar_olish(40)
#     print(q.jon_korish(), q.tirikmi())

# q.davolanish(50)
# print(q.jon_korish(), q.tirikmi())





# class Seyf:
#     def __init__(self, pin, ichida=None, ochiq=False, xatolar=0):
#         if ichida is None:
#             ichida = []
#         self.__pin = pin
#         self.__ichida = ichida
#         self.__ochiq = ochiq
#         self.__xatolar = xatolar

#     def ochish(self, kirgizilgan):
#         if kirgizilgan == self.__pin:
#             self.__ochiq = True
#         else:
#             self.__xatolar += 1

#     def yopish(self):
#         self.__ochiq = False

#     def ichiga_solish(self, qimmatbaho):
#         if self.__ochiq:
#             self.__ichida.append(qimmatbaho)
#         else:
#             print("Seyf yopiq")

#     def tashqariga_olish(self, qimmatbaho):
#         if self.__ochiq:
#             if qimmatbaho in self.__ichida:
#                 self.__ichida.remove(qimmatbaho)
#             else:
#                 print("Bunday narsa yo'q")
#         else:
#             print("Seyf yopiq")

#     def narsalar(self):
#         return self.__ichida

#     def pin_almashtirish(self, eski_pin, yangi_pin):
#         if eski_pin == self.__pin and self.__ochiq:
#             self.__pin = yangi_pin
#         else:
#             print("Noto'g'ri kiritildi")

#     def is_open(self):
#         return self.__ochiq


# kalit = Seyf(1234)
# for i in range(3):
#     kirgizilgan = int(input("Pinni kiriting: "))
#     kalit.ochish(kirgizilgan)
#     if kalit.is_open():
#         break

# print("Ichidagi narsalar:", kalit.narsalar())
# print("Ochiqmi?", kalit.is_open())
# kalit.yopish()
# print("Ochiqmi?", kalit.is_open())
# kalit.ochish(1234)
# kalit.ichiga_solish("Pul")
# print("Ichidagi narsalar:", kalit.narsalar())


    





# class kitob:
#     def __init__(self,nomi,nuxsa,berilgan=0):
#         self.__nomi = nomi
#         self.__nuxsa = nuxsa
#         self.__berilgan = berilgan

#     def olish(self):
#         if self.__berilgan < self.__nuxsa:
#             self.__berilgan += 1
#             return "Kitob berildi"
#         else:
#             return "Kitob yo'q"

#     def qaytarish(self):
#         if self.__berilgan > 0:
#             self.__berilgan -= 1
#             return "Kitob qaytarildi"
#         else:
#             return "Bunday kitob yo'q"


#     def mvjud(self):
#         return self.__nuxsa - self.__berilgan

#     def show(self):
#         return f"Nomi: {self.__nomi}, Nuxsa: {self.__nuxsa}, Berilgan: {self.__berilgan}"


# kitob = kitob("Python", 5, 2)
# print(kitob.show())
# print(kitob.mvjud())
# print(kitob.olish())
# print(kitob.show())
# print(kitob.qaytarish())
# print(kitob.show())







# class bank_karta:
#     def __init__(self,balans,kunlik_limit=1000000,bugun_sarflandi=0):
#         self.__balans = balans
#         self.__kunlik_limit = kunlik_limit
#         self.__bugun_sarflandi = bugun_sarflandi


#     def tolov(self,summa):
#         if summa>0 and self.__bugun_sarflandi+summa<= self.__kunlik_limit and self.__balans>=summa:
#             self.__balans-=summa
#             self.__bugun_sarflandi+=summa
#             return True
#         else:
#             return False


#     def kunlik_limit_qayta_tiklash(self):
#         self.__bugun_sarflandi = 0
#         return "Kunlik limit qayta tiklandi"


    
#     def pul_solish(self,summa):
#         if summa>0:
#             self.__balans+=summa
#             return True
#         else:
#             return False

#     def yangi_kun(self):
#         self.__bugun_sarflandi = 0


#     def qoldiq(self):
#         return self.__kunlik_limit - self.__bugun_sarflandi


#     def show(self):
#         return f"Balans: {self.__balans}, Kunlik limit: {self.__kunlik_limit}, Bugun sarflandi: {self.__bugun_sarflandi}"

# karta = bank_karta(1000000)
# print(karta.tolov(200000))
# print(karta.tolov(800000))
# print(karta.tolov(200000))
# print(karta.kunlik_limit_qayta_tiklash())
# print(karta.tolov(1000000))







# class uyhayvoni:
#     def __init__(self,ism,ochlik=100,kayfiyat=100,energiya=100):
#         self.__ism=ism
#         self.__ochlik=ochlik
#         self.__kayfiyat=kayfiyat
#         self.__energiya=energiya


#     def ovqat(self):
#         if self.__ochlik+25<=100 and self.__energiya+20>=0:
#             self.__ochlik+=25
#             self.__energiya-=20
#             return True
#         else:
#             return False


#     def uxlash(self):
#         if self.__energiya+25<=100 and self.__ochlik-20>=0:
#             self.__energiya+=25
#             self.__ochlik-=20
#             return True
#         else:
#             return False

#     def uynash(self):
#         if self.__kayfiyat+25<=100 and self.__energiya-20>=0:
#             self.__kayfiyat+=25
#             self.__energiya-=20
#             return True
#         else:
#             return False

#     def qoldiq(self):
#         return self.__ochlik,self.__kayfiyat,self.__energiya
#     def show(self):
#         return f"Ism: {self.__ism}, Ochlik: {self.__ochlik}, Kayfiyat: {self.__kayfiyat}, Energiya: {self.__energiya}"

# hayvon1 = uyhayvoni("Tom", 50, 60, 70)
# print(hayvon1.ovqat())
# print(hayvon1.uxlash())
# print(hayvon1.uynash())
# print(hayvon1.qoldiq())
# print(hayvon1.show())







# class avtomobil:
#     def __init__(self,model,benzin=0,tezlik=0,yurgan_masofa=0):
#         self.__model=model
#         self.__benzin=benzin
#         self.__tezlik=tezlik
#         self.__yurgan_masofa=yurgan_masofa

#     def benzin_quyish(self,litr):
#         if self.__benzin+litr<=50:
#             self.__benzin += litr
#             return True
#         else:
#             return False


#     def gaz_berish(self,gaz):
#         if self.__tezlik == 0:
#             self.__tezlik += gaz
#             return True
#         else:
#             return False

#     def tormoz(self):
#         if self.__tezlik>0:
#             self.__tezlik=0
#             return True
#         else:
#             return False


#     def yurish(self,km):
#         if self.__tezlik>0 and self.__benzin>0:
#             self.__yurgan_masofa+=km
#             self.__benzin-=km*0.1
#             return True
#         else:
#             return False


# m = avtomobil('Nexia')
# m.benzin_quyish(20)
# print(m.yurish(80))
# m.tormoz()


        
    
        
    


# class restoran_savati:
#     def __init__(self,mahsulotlar,chegirma=0):
#         self.mahsulotlar=mahsulotlar
#         self.chegirma=chegirma

#     def qoshish(self,nomi,narx,soni):
#         self.mahsulotlar.append([nomi,narx,soni])
    
#     def ochirish(self,nomi):
#         for i in self.mahsulotlar:
#             if i[0]==nomi:
#                 self.mahsulotlar.remove(i)
#                 return True
#         return False
    
#     def promokod(self,kod):
#         if kod=="PAYME":
#             self.chegirma+=10
#         return True

#     def jami(self):
#         summa=0
#         for i in self.mahsulotlar:
#             summa+=i[1]*i[2]
#         return summa*(1-self.chegirma/100)
    

# restoran = restoran_savati([],0)
# restoran.qoshish("Cola",10000,2)
# restoran.qoshish("Fanta",10000,2)
# restoran.promokod("PAYME")
# print(restoran.jami())







# class konditsioner:
#     def __init__(self, yoqilgi=False, harorat=24, rejim="avto"):
#         self.yoqilgi=yoqilgi
#         self.harorat=harorat
#         self.rejim=rejim

#     def yoqish(self):
#         self.yoqilgi=True
    
#     def ochirish(self):
#         self.yoqilgi=False
    
#     def harorat_qoshish(self,harorat):
#         if self.yoqilgi:
#             self.harorat+=harorat
    
#     def harorat_kamaytirish(self,harorat):
#         if self.yoqilgi:
#             self.harorat-=harorat
    
#     def rejim_almashtirish(self,rejim):
#         if self.yoqilgi:
#             self.rejim=rejim
    
#     def show(self):
#         return f"Yoqilgi: {self.yoqilgi}, Harorat: {self.harorat}, Rejim: {self.rejim}"

# konditsioner = konditsioner()
# print(konditsioner.yoqish())
# print(konditsioner.harorat_qoshish(2))
# print(konditsioner.harorat_kamaytirish(2))
# print(konditsioner.rejim_almashtirish("sovuq"))
# print(konditsioner.show())






# class Lift:
#     def __init__(self):
#         self.__qavat = 1
#         self.__yuk = 0
#         self.__max_yuk = 400
#         self.__eshik_ochiq = False

#     def kirish(self, vazn):
#         if self.__yuk + vazn > self.__max_yuk:
#             print("Ortiqcha yuk!")
#         else:
#             self.__yuk += vazn

#     def chiqish(self, vazn):
#         if vazn <= self.__yuk:
#             self.__yuk -= vazn
#         else:
#             print("Bunday yuk yo‘q!")

#     def qavatga_bor(self, n):
#         if self.__eshik_ochiq:
#             print("Eshikni yoping!")
#         else:
#             self.__qavat = n
#             print(f"Lift {n}-qavatga bordi.")

#     def eshik_ochish(self):
#         self.__eshik_ochiq = True

#     def eshik_yopish(self):
#         self.__eshik_ochiq = False

#     def holat(self):
#         print(f"Qavat: {self.__qavat}, Yuk: {self.__yuk} kg, "
#               f"Eshik {'ochiq' if self.__eshik_ochiq else 'yopiq'}")











# class Jurnal:
#     def __init__(self, sinf):
#         self.sinf = sinf
#         self.__baholar = {}  

#     def talaba_qoshish(self, ism):
#         if ism not in self.__baholar:
#             self.__baholar[ism] = []
#         else:
#             print("Bu talaba allaqachon mavjud.")

#     def baho_qoyish(self, ism, baho):
#         if ism not in self.__baholar:
#             print("Bunday talaba yo'q!")
#             return
#         if baho < 2 or baho > 5:
#             print("Noto'g'ri baho!")
#             return
#         self.__baholar[ism].append(baho)

#     def ortacha(self, ism):
#         if ism not in self.__baholar or len(self.__baholar[ism]) == 0:
#             return None
#         return sum(self.__baholar[ism]) / len(self.__baholar[ism])

#     def eng_yaxshi(self):
#         if not self.__baholar:
#             return None
#         return max(self.__baholar, key=lambda ism: self.ortacha(ism))

#     def hisobot(self):
#         for ism, baholar in self.__baholar.items():
#             print(f"{ism}: {baholar}, o'rtacha = {self.ortacha(ism)}")
