matriz = []    #sem os numeros no colchete cria a lista vazia que armazena todas as listas

for i in range(4): #aqui o laço controla as linhas repetindo 4x e criando 4 linhas 
    linha = []     #cria uma linha nova e vazia a cada repetição 
    for j in range(4): #aqui o laço controla as colunas msm esquema que os das linhas 
        linha.append(0)  # add o valor 0 na linha 
    matriz.append(linha) # adiciona a linha completa na matriz
    
    print(matriz)