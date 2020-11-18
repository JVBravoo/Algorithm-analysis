# Introdução:
## O problema da mochila é um clássico na computação.
## Seu desafio é maximizar o precoor dentro da mochila sem extrapolar o peso, você como excelente aluno de programação aceitou esse desafio. 
## Consiste em escolher itens de uma lista, cada item tem duas característica um peso e precoor.

# Formato da entrada:
## Dado dois inteiros N e P sendo, respectivamente o tamanho lista dos itens e a capacidade da mochila e será dada mais duas linhas com N números inteiros, 
## a primeira linha corresponde aos precoores dos itens e a segunda linha corresponde ao peso do item. 
## A posição i-th corresponde ao precoor do item e o peso dele na lista.
## 1 <= N <= 10
## 1 <= P <= 1000

# N = tamanho lista dos itens
# P = capacidade da mochila

# Formato da saída:
## Um linha com um inteiro corresponde maior valor que pode ser levado na mochila.

def problema_mochila(bag, kg, preco, n): 
    arr = [[0 for x in range(bag + 1)] for x in range(n + 1)] 
  
    for i in range(n + 1): 
        for j in range(bag + 1): 
            if i == 0 or j == 0: 
                arr[i][j] = 0
            elif kg[i-1] <= j: 
                arr[i][j] = max(preco[i-1] + arr[i-1][j-kg[i-1]],  arr[i-1][j]) 
            else: 
                arr[i][j] = arr[i-1][j] 
  
    return arr[n][bag] 


preco = []
kg = []

variavel = (input().split(" "))
n, bag = (int (x) for x in (variavel))
for p in input().split(" "):
    preco.append(int(p))
for k in input().split(" "):
    kg.append(int(k))

print(problema_mochila(bag, kg, preco, n))
