# -*- coding: utf-8 -*-
# Escreva um programa que compare se duas sequencias digitadas pelo usuario sao iguais.
import re

seq1 = "AT.G.*"
seq2 = "ATTGAAAA"

busca = re.match(seq1, seq2)

if busca:
    print("Sequencias identicas")
    print(busca.group())
else:
    print("Sequencias diferentes")