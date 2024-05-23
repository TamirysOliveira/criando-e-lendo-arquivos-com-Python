# -*- coding: utf-8 -*-

novo_arquivo = open('arq_teste.txt', "w")
novo_arquivo.write("Esse é um arquivo teste!")
novo_arquivo.close()

novo_arquivo = open('arq_teste.txt', "r")
texto_completo = novo_arquivo.read()
novo_arquivo.close()

print (texto_completo)
print ("\n")

novo_arquivo = open('arq_teste.txt', "a")
novo_arquivo.write("\nEssa é uma nova linha inserida\n")
novo_arquivo.close()

novo_arquivo = open('arq_teste.txt', "r")
texto_completo = novo_arquivo.read()
novo_arquivo.close()

print (texto_completo)