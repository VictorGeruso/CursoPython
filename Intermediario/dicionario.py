# -*- coding: utf-8 -*-
# Relação chave valor
nomes = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

print(nomes)

for chave in nomes:
    print(chave+"-"+nomes[chave])

for i in nomes.items():
    print(i)

for i in nomes.values():
    print(i)

for i in nomes.keys():
    print(i)