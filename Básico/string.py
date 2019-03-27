# -*- coding: utf-8 -*-
a = "Victor"
b = "Geruso"

concatenar = a + " " + b

print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

print(concatenar[0:6])

# Métodos String

print(concatenar.lower())
print(concatenar.upper())

c = "Olá"
d = "mundo"

concat = c + " " + d + "\n"

print(concat.strip())

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split()
print(minha_lista)

busca = minha_string.find("rei")
print(busca)

print(minha_string[busca:])

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)