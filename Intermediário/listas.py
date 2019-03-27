# -*- coding: utf-8 -*-
frutas = ["abacaxi", "melancia", "abacate"]
numeros = [1, 2, 3, 4, 5]
mista = ["abacaxi", 2, 9.89, True]

# Print das lista completas
print(frutas)
print(numeros)
print(mista)

# Print dos itens das listas
print(frutas[2])
print(numeros[0])
print(mista[3])

# Print de todos os itens de uma lista
for i in frutas:
    print(i)

# Inserindo novo valor na lista
frutas.append("limão")

# Pesquisando um valor em uma lista
if 3 in numeros:
    print("3 está na lista")

if 7 in numeros:
    print("7 está na lista")

# Remover item da lista
del frutas[2:]
print(frutas)

# Deletar todos os itens de uma lista
del frutas[:]
print(frutas)

# Criar lista em branco
lista = []
lista.append(57)
print(lista)

# Ordenação de listas
listaValores = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
listaValores.sort() # O metodo sort simpliesmente autera a lista para a ordenação
print(listaValores)
listaValores.sort(reverse=True) # Ordenado a lista em ordem decrescente
print(listaValores)
listaValores.reverse() # Inverte os valores da lista
print(listaValores)

listaValores_2 = [124, 567, 894, 7, 234, 3, 2, 6, 0, 67, 89, 1092]
listaValores_2 = sorted(listaValores_2) # O metodo sorted ele retorna uma lista ordenada
print(listaValores_2)

# Ordenar a lista em ordem alfabetica

palavras = ["Bola", "Abacate", "Dinheiro"]
palavras.sort()# Também se aplica o parametro reverse e o metodo reverse
print(palavras)