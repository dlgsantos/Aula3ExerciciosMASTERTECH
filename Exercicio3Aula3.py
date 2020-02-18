import random as rd
numero = int(input('Quantidade desejada na lista: '))
lista = rd.sample(range(0,1000),numero)
print(lista)
print(max(lista))
print(min(lista))

