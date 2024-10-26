#Zadanie 1
#A)
#Dodawanie
a=1 + 2
print('1.',a)
print ('To jest ',type ( a))
#Odejmowanie
b=1 + 4.5
print('2.',b)
print('To jest ',type(b))
#Dzielenie
c=3 / 2
print('3.',c)
print('To jest ',type (c))
#Dzielenie
d=4 / 2
print('4.',d)
print('To jest ',type (d))
#Dzielenie całkowite
e=3 // 2
print('5.',e)
print('To jest ',type (e))
#Dzielenie całkowite
f=-3 // 2
print('6.',f)
print('To jest ',type (f))
#Dzielenie modulo
g=11 % 2
print('7.',g)
print('To jest ',type (g))
#Potęgowanie
h=2 ** 10
print('8.',h)
print('To jest ',type (h))
#Potęgowanie
i=8 ** (1/3)
print('9.',i)
print('To jest ',type (i))

#B)
int(3.0)
print(int)

# Zadanie 2

uczelnia='Studiuje na WSIiZ'
print(uczelnia)

#Zadanie 3

imie= 'Jan'
wiek= 20
wzrost= 178
print('Nazywam się',imie,'i mam',wiek,"lat")
print('Mój wzrost to',wzrost,"cm")

#Zadanie 4

cena=39.99
rabat=0.2
cena_rabat=cena * rabat

print("Cena produktu po rabacie:")
print(round(cena-cena_rabat,2))

#Zadanie 5
a=float(input('Podaj bok a:'))
b=float(input('Podaj bok b:'))

obwod=2 *(a+b)

pole=a * b

print('Obwód prostokąta wynosi:', obwod)
print('Pole prostokąta wynosi:',pole)


#Zadanie 6
trasa=float(input('Podaj długość przejechanej trasy :'))
spalanie=float(input('Podaj średnie spalanie l/100km:'))
cena_paliwa=float(6.5)
3
zuzycie = (spalanie / 100) *  trasa

koszt = zuzycie * cena_paliwa

print('Zużycie paliwa wyniesie:',zuzycie)
print('Koszt paliwa to:',koszt)

#Zadanie 6A
import random
trasa = random.randint(100, 1000)

spalanie=float(input('Podaj średnie spalanie l/100km:'))
cena_paliwa=float(input('Podaj cenę paliwa za litr:'))
zuzycie = (spalanie / 100) *  trasa

koszt = zuzycie * cena_paliwa

print('Zużycie paliwa wyniesie:',zuzycie)
print('Koszt paliwa to:',koszt)

#Zadanie 6B
import random
trasa = random.randint(100, 1000)

spalanie=float(input('Podaj średnie spalanie l/100km:'))
cena_paliwa=float(input('Podaj cenę paliwa za litr:'))
zuzycie = (spalanie / 100) *  trasa

koszt = zuzycie * cena_paliwa

print(f'Zużycie paliwa wyniesie:{zuzycie}')
print(f'Koszt paliwa to:{koszt}')






