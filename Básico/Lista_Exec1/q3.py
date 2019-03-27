# -*- coding: utf-8 -*-
# Escreva um programa que resolva uma equação de segundo grau.
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2-4*a*c
raizDel = delta**(1/2)

x1 = (-b + raizDel)/(2*a)
x2 = (-b - raizDel)/(2*a)

print("x' = %f" %(x1))
print("x'' = %f" %(x2))