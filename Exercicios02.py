# Exercício 01 - Módulo 2
from re import I


n1 = int(input('Digite um número para o A: '))
n2 = int(input('Digite um número para o B: '))

if n1 > n2: 
    maior = n1
    print(f'O maior número é: {maior}, corresponde ao A.')

elif n2 > n1:
    maior = n2
    print(f'O maior número é: {maior}, corresponde ao B.')

else:
    print('Os dois números são iguais!')

print('Fim do programa!')



# Exercício 02 - Módulo 2
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 > n2 and n1 > n3: 
    print('Condição satisfeita!')
else:
    print('ERRO.')

print('Fim do programa!')



# Exercício 03 - Módulo 2
num = int(input('Insira um número inteiro: '))
resto_divisao = num % 2
# Se o número for par, a divisão é exata e o resto é sempre 0. Se o número for ímpar, sobra resto 1.

if resto_divisao == 0:
    print(f'O número {num}, é par.')
else:
    print(f'O número {num}, é impar.')

print('Fim do programa!')



# Exercício 04 - Módulo 2
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

if n1 == n2:
    resultado = (n1 * n2)
    print(f'A multiplicação entre {n1} x {n2} é {resultado}.')
elif n1 > n2:
    resultado = (n1 - n2)
    print(f'A subtração entre {n1} - {n2} é {resultado}.')
else:
    print(f'A soma entre {n2} + {n1} é {n2 + n1}.')

print('Fim do programa.')



# Exercício 05 - Módulo 2
print('Calculadora com dois números inteiros.')
n1 = int(input('Insira o 1º valor: '))
n2 = int(input('Insira o 2º valor: '))

print(' Digite 1 para: SOMAR\n Digite 2 para: SUBTRAIR\n Digite 3 para: MULTIPLICAR\n Digite 4 para: DIVIDIR')
digito = int(input('Selecione a opção: '))

if digito == 1:
    print(f'A soma entre {n1} + {n2} = {n1 + n2}')
elif digito == 2:
    print(f'A subtração entre {n1} - {n2} = {n1 - n2}')
elif digito == 3:
    print(f'A multiplicação entre {n1} x {n2} = {n1 * n2}')
elif digito == 4:
    if n2 != 0:
        resultado = n1 / n2
        print(f'A divisão entre {n1} / {n2} = {resultado}')
    else:
        print('Divisão por zero')
else:
    print('ERRO. Tente novamente')
print('Fim do programa!')



# Exercício 06 - Módulo 2
print('Cálculos de um retângulo.')
base = float(input('Insira a base: '))
altura = float(input('Insira a altura: '))

print('Opções de processamento:')
print('Insira 0 para calcular o perímetro.')
print('Insira 1 para calcular a área.')

opc = int(input('Digite a sua opção: '))

if opc == 0:
    perimetro = (base + altura) * 2
    print(f'O Perímetro é de {perimetro:.2f}m')
elif opc == 1:
    area = base * altura 
    print(f'A Área é de {area:.2f}m')
elif opc < 0 or opc > 1:
    print('Opção invalida!')
    
print('Fim do programa!')



# Exercício 07 - Módulo 2
print('Sistema de média com conceito')

nota1 = float(input('Insira a nota do trabalho: '))
nota2 = float(input('Insira a nota da avaliação: '))
nota3 = float(input('Insira a nota do exame: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 8:
    print('Conceito A')
elif media >= 7:
    print('Conceito B')
elif media >= 6:
    print('Conceito C')
elif media >= 5:
    print('Conceito D')
else:
    print('Conceito E')

print('Fim do programa!')


# Exercício 08 - Módulo 2
print('Sistema de aprovação escolar!')

nota1 = float(input('Insira a 1º nota: '))
nota2 = float(input('Insira a 2º nota: '))
nota3 = float(input('Insira a 3º nota: '))

media = (nota1 + nota2 + nota3) / 3

# Validação para garantir que a média está entre 0 e 10
if media > 10 or media < 0:
    print('Erro: Média inválida! Certifique-se de que as notas estão entre 0 e 10.')
else:
    print(f'Média: {media:.2f}')
    
    if media >= 7:
        print('Aprovado! Parabéns.')
    elif media >= 3:
        print('Exame.')
    else:
        print('Reprovado!')

print('Fim do programa!')



# Exercício 09 - Módulo 2
n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))
n3 = int(input('Insira o 3º número: '))

# Coloca os números em uma lista e ordena
numeros = sorted([n1, n2, n3])

print(f"{numeros[0]} - {numeros[1]} - {numeros[2]}")



# Exercício 10 - Módulo 2
n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))
n3 = int(input('Insira o 3º número: '))
n4 = int(input('Insira o 4º número: '))

numeros = [n3, n2, n1, n4]
print(f"{numeros[2]} - {numeros[1]} - {numeros[0]} - {n4}")



# Exercício 11 - Módulo 2
import math

a = int(input('Insira o coeficiente a: '))
b = int(input('Insira o coeficiente b: '))
c = int(input('Insira o coeficiente c: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('Raízes fora do domínio dos números reais.')
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print('Raiz x\':', x1)
    print('Raiz x\'\':', x2)



# Exercício 12 - Módulo 2
a = float(input('Insira o 1º valor: '))
b = float(input('Insira o 2º valor: '))
c = float(input('Insira o 3º valor: '))

print('Opções sobre os valores: 1, 2 e 3')
print('Opção 1: Valores em ordem crescente')
print('Opção 2: Valores em ordem decrescente')
print('Opção 3: O maior fica entre os outros dois')
escolha = int(input('Digite a opção desejada: '))

numeros = sorted([a, b, c])

if escolha == 1:
    print(f'A ordem fica: {numeros[0]} - {numeros[1]} - {numeros[2]}')

elif escolha == 2:
    print(f'A ordem fica: {numeros[2]} - {numeros[1]} - {numeros[0]}')

elif escolha == 3:
    if a > b and a > c:
        maior = a
        print(f'A ordem fica: {b} - {maior} - {c}')
    elif b > a and b > c:
        maior = b
        print(f'A ordem fica: {a} - {maior} - {c}')
    else:
        maior = c
        print(f'A ordem fica: {a} - {maior} - {b}')
else:
    print('Opção invalida!')



# Exercício 13 - Módulo 2
from math import sqrt

print('-' * 5, 'Menu de opções', '-' * 5)
print('1 - Somar dois números;')
print('2 - Raiz quadrada de um número;')

opc = int(input('Digite a opção: '))

if opc == 1:
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
    soma = n1 + n2
    print(f'O resultado da SOMA é: {soma}')
elif opc == 2:
    valor = int(input('Insira o valor para saber a raiz quadrada: '))
    raiz_valor = sqrt(valor) 
    print(f'O resultado da RAIZ é: {raiz_valor}')
else:
    print('Opção invalida!')
print('Fim do programa.')



# Exercício 14 - Módulo 2
print('-' * 30)
print('Calculadora de Duração de Jogo')
print('-' * 30)

# Entrada da hora de início
hora_inicial = int(input('Hora de início (0-23): '))
minuto_inicial = int(input('Minuto de início (0-59): '))

# Entrada da hora de término
hora_final = int(input('Hora de término (0-23): '))
minuto_final = int(input('Minuto de término (0-59): '))

# Convertendo o horário inicial e final totalmente para minutos
inicio_em_minutos = (hora_inicial * 60) + minuto_inicial
fim_em_minutos = (hora_final * 60) + minuto_final

# Se o horário final for menor ou igual ao inicial, significa que o jogo passou da meia-noite (dia seguinte)
if fim_em_minutos <= inicio_em_minutos:
    fim_em_minutos += 1440 # Adicionamos 24 horas em minutos (24 * 60 = 1440)

# Calculando a diferença total em minutos
duracao_total_minutos = fim_em_minutos - inicio_em_minutos

# Convertendo os minutos totais de volta para horas e minutos
duracao_horas = duracao_total_minutos // 60
duracao_minutos = duracao_total_minutos % 60

# Exibindo o resultado formatado
print('-' * 30)
print(f'O jogo durou {duracao_horas} hora(s) e {duracao_minutos} minuto(s).')
print('-' * 30)



# Exercício 15 - Módulo 2
print('-' * 5, 'Salário conforme bonificação', '-' * 5)
salario = float(input('Informe o seu salário: R$'))

if salario <= 500.00:
    salario_ajustado = salario + (salario * 5) / 100
    print(f'Seu salário ajustado é de: R${salario_ajustado:.2f}')

elif salario <= 1200.00:
    salario_ajustado = salario + (salario * 12) / 100
    # Verifica o auxílio escola para quem ganha até 600
    if salario <= 600.00:
        aux_escola = 150.00
        salario_ajustado2 = salario_ajustado + aux_escola
        print(f'Seu salário com auxílio-escola é de: R${salario_ajustado2:.2f} (Inclui R$ {aux_escola:.2f} de auxílio)')
    else:
        print(f'Seu salário ajustado é de: R${salario_ajustado:.2f}')

else:
    salario_ajustado = salario + 600.00
    print(f'Seu salário com acréscimo fixo é de: R${salario_ajustado:.2f}')
print('Fim do programa!')
