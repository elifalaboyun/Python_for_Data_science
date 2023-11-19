#Examine data structures of values

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

t = ("machine learning", "Data Science")
type(t)

s = {"python", "machine learning", "data science"}
type(s)

#Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
#kelime kelime ayırınız.


text = "The goal is to turn data into information and information into insight."
text.upper().replace(",", " ").replace(".", " ").split()

##########################################################################
#gÖREV 3: VERİLEN LİSTE İÇİN AŞAĞIDAKİ GÖREVLERİ YAPINIZ
##############################################################
lst =["D","A","T","A","S","C","I","E","N","C","E"]

len(lst)

lst[0]
lst[10]


data_list = lst[0:4]
data_list

#8. indexteki elemanı silin
lst.pop(8)
lst

#yeni bir eleman ekle
lst.append(101)
lst

#sekizinci indexe "N" elemanını tekrar ekleyin

lst.insert(8, "N")
lst

###################################################
#GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız
############################################

dict = {'Christian': ["America", 18],
        'Daisy':["England", 12],
        'Antonio':["spain", 22],
        'Dante' :["Italy", 25]}

#Adım 1 key değerlerine ulaşınız

dict.keys()

#adım 2 valuelara erişiniz
dict.values()

#adım 3 Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz
dict.update({"Daisy": ["England", 13]})
dict

#Adım 4: Key değeri Ahmet value değeri [Turkey,24 olan yeni bir değer ekleeyiniz

dict.update({"Ahmet": ["Turkey", 24]})
dict


#Adım 5: Antonio'yu listeden siliniz

dict.pop("Antonio")



############################################
#GÖREV 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere
#atayan ve bu listeleri  return eden fonksiyon yazınız.
################################################

l = [2, 13, 18, 93, 22]

def func(list):

    çift_list = []
    tek_list = []


    for i in list:
        if i % 2 == 0:
            çift_list.append(i)
        else:
            tek_list.append(i)

    return çift_list, tek_list

çift,tek = func(l)

#list comp. çözümü.

####################################################
#GÖREV 6: aşağıda verilen listede mühendislik ve tıp fakültelerinde dereceye giren öğrenciler
#sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenciler tıp fakülltesinin başarısını temsil etmektedir
#enumarate kullanarak öğrenci derecelerini fakülte özelinde yazınız.
#####################################################

ogrenciler = ["Ali", "Veli","Ayşe ","Talat", "Zeynep", "Ece"]
for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci",x)

    else:
        i -= 2
        print("Tıp fakültesi",i,". öğrenci",x)

########################################################
#Görev 7:Aşağıda 3 Adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi, kontenjanı verilmişt
##########################################


ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi,kontenjan):
    print(f"Kredi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


####################################################
#Görev 8: Aşağıda 2 adet set verilmiştir.
#Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor
##################################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda"," python", "miuul"])

def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1, kume2)
kume(kume2, kume1)