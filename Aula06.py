#Aula 06 - Questão 01
x=float(input('Digite o 1º número '));
y=float(input('Digite o 2º número '));
if(x>y):
    print('O 1º número é maior que o 2º')
else:
    print('O 1º número NÃO é maior que o 2º')

#Aula 06 - Questão 02
peso = float(input('Digite o peso '));
altura = float(input('Digite a altura '));
imc = float(peso / (altura * altura))
if( imc >= 18.5 and imc <= 24.9 ):
    print('a pessoa está no peso ideal de acordo com o IMC')
else:
    print('a pessoa NÃO está no peso ideal de acordo com o IMC')

#Aula 06 - Questão 03
idade = float(input('Digite a idade do nadador: '));
if(idade >= 18):
   print('O nadador é adulto')
elif (idade >= 11):
   print('O nadador é juvenil')
elif (idade >= 5):
   print('O nadador é infantil')
else:
   print('O nadador não tem a idade mínima')