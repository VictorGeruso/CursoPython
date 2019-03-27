# -*- coding: utf-8 -*-
# Estruturas condicionais
x = 1
y = 1000000

if x > y:
    print("x é maior que y")

if y > x:
    print("y é maior que x")

# else
x = 1
y = 2

if x > y:
    print("x é maior que y")
else:
    print("x não é maior que y")

#elif

x = 4
y = 5

if x == y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes")