#####################################################
#Fonskiyonlar, koşullar, döngüler, comprehensions
################################################

# - fonksiyonlar (functions)
# - Koşullar (conditions)
# - döngüler (loops)
# - comprehensions

############################
# foksiyon okur yazarlığı
##############################
print("a")

?print

print("a", "b")
print("a", "b", sep="__") #iki alt tire ile ayır demek


############################
# fonksiyon tanımlama
##########################


def calculate(x):
    print(x*2)


calculate(5)

#iki argümanlı iki parametreli bir fonksiyon tanımlayalım
def summer(arg1, arg2):
    print(arg1 + arg2)

summer(7, 8)

summer(arg2=8, arg1=7)

#########################33333
#docsttring
#############################

def summer(arg1, arg2):
    """

    :param arg1:
    :param arg2:
    :return:
    """
    print(arg1 + arg2)

