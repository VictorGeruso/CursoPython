# Manipulando um arquivo
arquivo = open("arquivo.txt")
linhas = arquivo.readlines()
for linha in linhas:
    print(linha)

# criando um arquivo
w = open("arquivo2.txt", "w")
w.write("Esse eh o meu arquivo")
w.close()

# Editando arquivo
a = open("arquivo.txt", "a")
a.write("Esse eh o meu arquivo\n")
a.close()
