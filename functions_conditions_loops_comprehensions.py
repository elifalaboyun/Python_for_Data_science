#####################################################
# Fonskiyonlar, koşullar, döngüler, comprehensions
################################################

# - fonksiyonlar (functions)
# - Koşullar (conditions)
# - döngüler (loops)
# - comprehensions

############################
# foksiyon okur yazarlığı
##############################
print("a")

print

print("a", "b")
print("a", "b", sep="__")  # iki alt tire ile ayır demek


############################
# fonksiyon tanımlama
##########################


def calculate(x):
    print(x * 2)


calculate(5)


# iki argümanlı iki parametreli bir fonksiyon tanımlayalım
def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)

summer(arg2=8, arg1=7)


#########################33333
# docsttring üç tane tırnak koyup entera basınca çıkıyor
#############################

def summer(arg1, arg2):
    """
     sum of two numbers
    :param arg1: int, float
    :param arg2: int,float
    :return: int, float
    """
    print(arg1 + arg2)


#############################################
# fonksiyonların statement/body bölümü
##############################################


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)

add_element(18, 9)


##################################
# ön tanımlı argümanlar/parametreler(default parameter/arguments)
######################################3


def divide(a, b):
    print(a / b)


divide(2, 4)

##################################
# ne zaman fonksiyona ihtiycaımız olur
############################################

# warm, moisture, charge
(56 + 15) / 80


# dry rule (dont repeat yourself)
def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)


##################################################
# Return: Fonksiyon çıktılarını girdi olarak kullanmak
##################################################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(98, 12, 78) * 10

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(98, 12, 78) * 10


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output


calculate(98, 12, 78)
type(calculate(98, 12, 78))  # böylece kaydetmiş oluruz değerleri


#######################################
# fonksiyon içerisinden fonksiyon çağırmak
####################################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(98, 12, 78) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


def all_calcuation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calcuation(1, 3, 5, 12)

###########################################
# lokal  global değişkenler(Local & global variables)
##########################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


#####################################
# koşullar(conditiond)
#####################################

if 1 == 1:
    print("something")

number = 11

if number == 10:
    print("number is 10")


def number_check(number):
    if number == 10:
        print("number is 10")


number_check(10)


#########################
# else
###########################

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(15)


##############################
# elif
############################
def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than  10")
    else:
        print("equal to 10")


number_check(9)

###############################
# döngüler (loops)
############################

# for loop

students = ["john", "Mark", "venessa", "mariam"]

students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20 / 100 + salary))


def new_salary(salary, rate):
    return (salary * rate / 100 + salary)


new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary, 2))

salaries2 = [1300, 2000, 3040, 4040, 5030]

for salary in salaries2:
    print(new_salary(salary, 10))

    salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salaries >= 3000:
        print(new_salary(salary, 42))
    else:
        print(new_salary(salary, 20))


###################################
#uygulama mülakat sorusu
#####################################

#amaç: aşağıdaki gibi string değiştiren bir fonksiyon yazmak istiyoruz

#beffore:"hi my name is john and ı am leaning python"

#after:"Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"      tek indekstekiler küçük çift indekstekiler büyük olacak


range(len("miuul"))
range(0, 5)

for i in range(len("miuul")):
    print(i)


def alternating(string):
    new_string = ""
    #girilen stringin indexlerinde gez.
    for string_index in range(len("string")):
        #string çift ise  büyük harfe çevir
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
            #index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower()
    print(new_string)
######################################
# break & continue & while
####################################
#break:akışı kesmeye yarar
#continue : ilgili şart gözlemlendiğinde akışta o şarta atlayarak devam etmeye
#while: bir koşul sağlandığı sürece devam etmeye yarayan ifadelerdir


salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue
    print(salary)


number = 1
while number < 5:
    print(number)
    number += 1

###############################
#enumerate: Automatic counter/ındexer ile for loop örnek: aşağıdaki listede hem öğrencilerin valuesunu gezme hem de indexlerini söyleme bilgisi veriyor
#########################

students = ["john", "Mark", "venessa", "Mariam"] #indexi çift olanlara bir işlem tek olanlara başka bir işlem

for student in students:
    print(student)

for index, student in enumerate(students): #genelde index numaraları 0 dan başlıyor ama birden başlatmak istersek (student , 1) yazarak birden başlatabiliriz
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)


#####################################################
#UYGULAMA MÜLAKAT SORUSU/Enumerate
######################################################
#divide_students fonksiyonu yazınız.
#çift indexte yer alan öğrencileri bir listeye alınız
#tek indexte yer alan öğrencileri başka bir listeye alınız
#fakat bu iki liste tek bir liste olarak return olsun

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)


    print(groups)

    return groups


st = divide_students(students)
st[0][1]

#########################################
#alternating fonksiyonunun enumerate ile yazılması
##################################


def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

    alternating_with_enumerate("hi my name is john and i am learning python")


############################
#zip
###############################

students = ["john", "mark", "venessa","mariam"]

department = ["mathematic", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]


list(zip(students, department, ages)) # ayrı ayrı listelerde aynı indexte bulunan elemanları tuple formunda 4 ayrı tuple yazıp bir listenin içine koydu

#########################################
#lambda, map, filter, reduce
##########################################

def summer(a,b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b

new_sum(4, 5)

# map

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)
for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))

list(map(lambda x: x * 20 / 100 + x, salaries))
#del new_sum

#FILTER

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x % 2 == 0, list_store))

#reduce

from functools import reduce
list_store = [1, 2, 3, 4]

reduce(lambda a, b: a + b, list_store)