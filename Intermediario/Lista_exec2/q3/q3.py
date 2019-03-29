# -*- coding: utf-8 -*-
# Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato fasta.
armSeq = open("ArmazemDeSequencias.fasta", "a")
seq = input("Digite a sequencia desejada: ")
armSeq.write(seq+"\n")
armSeq.close()
