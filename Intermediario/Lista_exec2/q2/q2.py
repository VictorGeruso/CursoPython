# Escreva um programa que abra um arquivo digitado pelo usuario e imprima seu conteudo na tela.
arquivo = open("arquivo.txt", "a")
escrita = raw_input("Digite qualquer coisa: ")
arquivo.write(escrita+"\n")
arquivo.close()

lerArquivo = open("arquivo.txt")
linhas = lerArquivo.readlines()
for linha in linhas:
    print(linha)
lerArquivo.close()