###############################
# Veri yapıları(data structures)
######################################
# - veri yapılarına giriş ve hızlı özet
# - sayılar(numbers): int, float, complex
# - karakter dizileri (strings) : str
# - boolean (true-false): bool
# - liste (list)
# - sözlük(diztionary)
# - demet (tuple)
# -  set
###############################
# Veri yapıları(data structures) giriş ve hızlı özet
######################################

#sayılar: integer
x = 46
type(x)

#sayılar : float
x = 10.3
type(x)

#complex sayılar
x = 2j + 1
type(x)

#string: karakter dizisi
x = "hello ai era"
type(x)

#boolean
True
False
type(True)
5 == 4
type(5 == 4)


#liste

x = ["btc", "eth", "xrp"]
type(x)


#Sözlük
x = {"name": "Peter", "Age": 36} #elemanlar virgül ile ayrılır name bir key dir valuesu da peterdır
type(x)

#tuple
x = ("python", "ml", "ds")
type(x)

#set
x = {"python", "ml", "ds"}
type(x)

#bu yukardakilerin hepsi python array olarak da geçmektedir(liste tuple set ve sözlük yapıları)
a = 5
b = 10.5
###########################
#tipleri değiştirmek
##########################
int(b)
float(a)
##########################################
#KARAKTER DİZİLERİ
########################################

print("john")
print('john')

name = "john"


##############################
# çok satırlı karakter dizisi
################################

"""ver yapıları: hızlı özet, sayılar(numbers): int, float, complex,
karakter dizileri ( string): str, list, dictionary, tuple, set,
boolean (true-false): bool"""

long_str = """ver yapıları: hızlı özet, sayılar(numbers): int, float, complex,
karakter dizileri ( string): str, list, dictionary, tuple, set,
boolean (true-false): bool""" #outputta çıkan /n ler o ifadenin bir satır aşağıda olduğunu gösterir


#########################################
#karakter dizilerinin elemanlarına erişmek
##########################

name
name[0]
name[2]

##köşeşli parantez koyunca benden bir index isteyeccek olarak algılıyor


#########################################
#karakter dizilerinde slice işlemi
#######################################
name = "john"

name[0:2]# sıfırdan başla 2 ye kadar git 2 hariç

long_str[0:10]



##############################################
#STRİNG İÇERİSİNDE KARAKTER SORGULAMAK
###############################################

long_str

"veri" in long_str
"ver" in long_str
"bool" in long_str


##############################################
# string metodları(sınıflar iççinde tanımlanan fonksiyonlardır
#############################################


dir(int) # int ile kullanılabilecek metodları gösteriyor

##########################33
#len(fonskiyon gömülü bir fonskiyon)
########################

name ="john"
type(name)
type(len)

len(name) #stringlerde boyut bilgisine ulaşmak için
len("elifalaboyun")

#kullanmış olduğumuz bir yağının metod mu yoksa fonksiyon mu olduğunu nasıl anlarız?:eğer bir fonskiyon class yapısı içeriinde tanımlandıysa metod denir tanımlanmadıysa func. denir.




###################
# upper() lower() : küçük-büyük dönüşşümleri
#####################
"miuul".upper()#nokta şey demek ben bundan önceki şeiyn string olduğunu algıladım ve sana kullanabileceğin bütün metodları sıralıyorum
"MIUUL".lower()

#########################################
#replace: karakter değiştirir
###########################

hi = "hello AI era"
hi.replace("l" , "y")

########################
#split: böler
##################
"hello AI era".split()


##############################
# strip : kırpar
############################
" ofoofof ".strip()
"ofoofof".strip("o")


##########################
#capitalize : ilk harfi büyütür
#############################

"foo".capitalize()


"foo".startswith("f")


#################
#list
###############################

# - değiştirilebilir
# - sıralıdır.Index işlemleri yapılabilir.
# - kapsayıcıdır

notes = [1, 2, 3, 4]
type(notes)


names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True,[1, 2, 3,] ]
type(not_nam)
len(not_nam)
not_nam[0]
not_nam[5]
not_nam[6][1]
notes = [1, 2, 3, 4]
notes[0] = 99

##############################
#liste metodları(list methods)
####################
dir(notes) #apend metodunu adın soyadın gibi bil

################################
#len: buildin python fonksiyonu, boyut bilgisi.
#############################
len(notes)
len(not_nam)

################################
#apend: eleman ekler
#############################
notes
notes.append(100)

###############################
#pop: indexe göre siler
#############################
notes.pop(0)

#############################
#insert: indexe ekler
###########################

notes.insert(2, 99)


#####################################
#sözlük(dictionary)
#############

#değiştirilebilir
#sırasız (3.7 sürümünden sonra sıralı)
#kapsayıcı

#key-value

dictionary = {"REG": "regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}
dictionary["REG"] #REG bir keyworddür regression ise onun valuesudur


##################################
#key sorgulama
##############################

"REG" in dictionary


#############################
#key e göre value ya ulaşmak
########################
dictionary["REG"]
dictionary.get("REG")


#######################
#value değiştirmek
######################

dictionary["REG"] = ["YSA", 10]

####################################
#tüm keylere erişmek
#############################

dictionary.keys()

dictionary.values()

############################
#tüm çiftleri tuple halinde listeye çevirme
##################################

dictionary.items()


##############################3
#key-calue değerini güncelleme
###############################
dictionary.update({"REG": 11})

########################################
#yeeni key-value değeri eklemek
#####################################
dictionary.update({"RF": 10})


#####################
#demet(tuple
#####################

#değiştirilemez
#sıralıdır
#kapsayıcıdır

t = ("john", "mark", 1, 2)
type(t)

t[0]

#değişiklik yapmak için ilk önce listeye çevirip sonra ekliyoruz sonra tekrar tuple a çevirebiliriz

t = list(t)
t[0] = 99
t = tuple(t)


################################
#set kümeler gibi düşünülebilir hız gerektiren işlemlerde kesişimleri nedir? birleşimleri nedir? ikisinin farkı nedir?
##########################33333

#değiştirilebilir
# sırasız+ eşsizdir
#kapsayıcıdır



##############################
#difference(): iki kümenin farkı
##########################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

#set1 de olup set 2 de olmayanlar

set1.difference(set2)
set2.difference(set1)
set1 - set2

################################################
#symmetric_difference(): iki kümede de birbirlerine göre olmayanlar
##########################################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)


########################################
#intersection(): iki kümenin kesişimi
################################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])


set1.intersection(set2)
set2.intersection(set1)


set1 & set2 #matematiksel ifadesi de bu


##################################
#union(): iki kümenin birleşimi
###################################
set1.union(set2)



#################################
#isdisjoint(): iki kümenin kesişimi boş mu değil mi?
################################3
set1.isdisjoint(set2)


###########################
#issubset() bir küme diğer kümenin alt kümesi mi?
###########################


set1.issubset(set2)
set2.issubset(set1)

#######################################
#issuperset()bir küme diğer kümeyi kapsıyor mu?
#######################################

set2.issuperset(set1)
