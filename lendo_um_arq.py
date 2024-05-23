# -*- coding: utf-8 -*-

def ler_arquivo():
    caminho_do_arquivo = r"C:\Users\Tamirys\Documents\INDICE_CORRESP.txt"  #aqui estou buscando um arquivo de texto que fala sobre as funções INDICE e CORRESP do Excel
    #Se for testar o código em sua máquina, substitua o caminho acima para o caminho para o seu arquivo
    
    # Abrindo o arquivo
    arquivo = open(caminho_do_arquivo, 'r', encoding='utf-8')
    
    # Lendo o conteúdo do arquivo
    conteudo = arquivo.read()
    
    # Imprimindo o conteúdo
    print(conteudo)
    
    # Fechando o arquivo
    arquivo.close()

ler_arquivo()
