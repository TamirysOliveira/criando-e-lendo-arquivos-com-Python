def ler_arquivo():
    caminho_do_arquivo = r"C:\Users\Tamirys\Documents\INDICE_CORRESP.txt"  

    # Abrindo o arquivo
    arquivo = open(caminho_do_arquivo, 'r', encoding='utf-8')
    
    # Lendo o conteúdo do arquivo
    conteudo = arquivo.read()
    
    # Imprimindo o conteúdo
    print(conteudo)
    
    # Fechando o arquivo
    arquivo.close()

ler_arquivo()
