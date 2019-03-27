# -*- coding: utf-8 -*-
# Escreva um programa que ordene uma lista numérica com três elementos.

lista = [1000, 2, 75, 23, 89, 1, 0, 30, 54, 5, 7, 4]

for i in range(len(lista)):
    menor = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print(lista)