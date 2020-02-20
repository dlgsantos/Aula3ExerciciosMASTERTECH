import math
def calcula_area(r):
    area = (r**2)*math.pi
    return area
def calcula_perimetro(r):
    comprimento = 2*math.pi*r
    return comprimento
try:
    raio = float(input('Digite o tamanho do raio: '))
except:
    raio=0
    print('Digite valor numérico')
print('Uma circunferência de raio' ,raio, ' tem uma área de ', calcula_area(raio), ' e um comprimento de ',calcula_perimetro(raio))
