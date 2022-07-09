#Esse programa calcula a quantidade de gotas de uma receita pediátrica
print ("Este é o algoritmo conta gotas")
peso  = float(input('Digite o peso da criança: '))
qtdGotas = peso // 3
qtdGotas = qtdGotas * 2
print ("Quantidade de Gotas a ser tomada ", qtdGotas)