# 5) Escreva um programa que inverta os caracteres de um string.
#
#
# IMPORTANTE:
#
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#
# b) Evite usar funções prontas, como, por exemplo, reverse;


string = 'a b c d e f g'
lista_inicial = string.split() # transformando string em lista
lista_invertida = []


for i in range(len(lista_inicial)): #for loop baseado no número de elementos da lista
    lista_invertida.append(lista_inicial[-(i+1)]) #adicionando itens para a nova lista com base no índice negativo

string_invertida = ' '.join(lista_invertida) #transformando denovo em string

print(string_invertida)
