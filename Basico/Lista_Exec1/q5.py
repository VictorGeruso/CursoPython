# -*- coding: utf-8 -*-
# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

n1 = int(input("informe o primeiro numero: "))
sinal = input("informe o sinal da operação: ")
n2 = int(input("informe o segundo numero: "))

resultado = 0

if sinal == "+":
    resultado = n1 + n2
elif sinal == "-":
    resultado = n1 - n2
elif sinal == "*":
    resultado = n1 * n2
elif sinal == "/":
    resultado = n1 / n2
else:
    print("operador incorreto")

print(resultado)