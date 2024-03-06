# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.


sequencia = [0,1] #iniciar sequência como lista com os primeiros dígitos

input_numero_inteiro = int(input('Escolha um número inteiro para verificar:'))

def calcular_sequencia_de_fibonacci(input_para_calcular):
    while len(sequencia) < (input_para_calcular + 2): #adiciona +2 para compensar o fato de começar em 0 e repetir 1
        if sequencia[-1] < input_para_calcular: #somente calcula até, no máximo, o próximo número mais alto
            numero_atual = sequencia[-2] + sequencia[-1] #fazendo soma utilizando índices
            sequencia.append(numero_atual)
        else:
            break

calcular_sequencia_de_fibonacci(input_numero_inteiro)

if input_numero_inteiro in sequencia:
    print('O número faz parte da sequência de Fibonacci')
else:
    print('O número não faz parte da sequência de Fibonacci')



