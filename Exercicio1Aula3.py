
import datetime
a = int(input('Insira o ano de seu nascimento: '))
b = int(input('Insira o mes de seu nascimento: '))
c = int(input('Insira o dia de seu nascimento: '))
data_nascimento = datetime.date(year = a,month = b,day = c)
def calcula_dias_vida(data_nascimento):
    total_dias = datetime.date(2020,2,20) - data_nascimento
    return total_dias
print('Sua quantidade de dias vivos é: ', calcula_dias_vida(data_nascimento))