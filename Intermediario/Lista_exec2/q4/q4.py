# -*- coding: utf-8 -*-
# Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer.
# Se o usuário digitar 1, o programa deve chamar uma função que lê um arquivo de texto. 
# Se o usuário apertar 2, o programa deve imprimir o conteúdo do arquivo lido anteriormente. 
# Se o usuário apertar três o programa deve ser fechado.
print("Olá tudo bem?")
print("Seja bem vindo ao nosso sistema")
print("Se você deseja ler algum arqivo de texto digite 1.")
print("Se deseja que algum conteudo de algum arquivo seja impresso digite 2.")
print("Se deseja que deseja encerrar o program digite 3.")
op = input("informe a opção desejada: ")

if op == "1":
    print("Lendo arquivo informado")
elif op == "2":
    print("Impirmindo arquivo informado")
elif op == "3":
    print("Fecehando programa")
else:
    print("Informe uma opção válida")