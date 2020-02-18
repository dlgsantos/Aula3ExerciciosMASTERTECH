Dia = {1:'domingo',2:'segunda',3:'terça',4:'quarta',5:'quinta',6:'sexta',7:'sábado'}
num_digitado = int(input('Digite um número entre 1 e 7: '))
if num_digitado > 7:
    print('Erro, insira um número entre 1 e 7')
elif num_digitado < 1:
    print('Erro, insira um número entre 1 e 7')
else:
   resultado = Dia.get(num_digitado)
   print(resultado)
