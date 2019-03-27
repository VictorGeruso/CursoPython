# -*- coding: utf-8 -*-
# Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.  
idade = int(input("Informe a sua idade: "))

if idade >= 18 :
    print("Você é maior")
elif idade < 0 :
    print("Idade inválida")
else:
    print("Você é menor")
    