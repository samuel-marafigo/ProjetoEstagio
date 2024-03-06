# 1) Observe o trecho de código abaixo:
#
# int INDICE = 13, SOMA = 0, K = 0;
#
# enquanto K < INDICE faça
#
# {
#
# K = K + 1;
#
# SOMA = SOMA + K;
#
# }
#
# imprimir(SOMA);
#
#
#
# Ao final do processamento, qual será o valor da variável SOMA?


k = 0
soma = 0
index = 13

while k < index:
    print(f'{k}/13')
    k = k + 1
    print(f'K + 1: {k}')
    print(f'soma anterior: {soma}')
    soma = int(soma) + int(k)
    print(f'soma atual: {soma}')
print(soma)