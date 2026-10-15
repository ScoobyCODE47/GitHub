from math import pi, sum, exp2, sqrt
from datetime import date

# Exercício 01 - Módulo 1
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))
resultado = sum([num1, num2, num3, num4])

print(f'O resultado da soma: {resultado}')
print('Fim do programa.')



# Exercício 02 - Módulo 1
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

print(f'A média das notas é: {media:.2f}')
print('Fim do programa.')



# Exercício 03 - Módulo 1
n1 = float(input('Insira a primeira nota: '))
p1 = float(input('Insira o peso da primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
p2 = float(input('Insira o peso da segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
p3 = float(input('Insira o peso da terceira nota: '))
media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(f'Média ponderada: {media:.2f}')
print('Fim do programa.')



# Exercício 04 - Módulo 1
salario = float(input('Digite o salário do funcionário: R$'))
print(f'O salário do funcionário é R${salario:.2f}')
salario_ajustado = ((salario * 25) / 100) + salario # Salário * 25 por(porcento) 100 do salário, e somo o salário para obter o valor do salário ajustado.

print(f'Com o aumento de 25%, o novo salário será R${salario_ajustado:.2f}')
print('Fim do programa.')



# Exercício 05 - Módulo 1
salario = float(input('Digite o salário do funcionário: R$'))
aumento = float(input('Digite o percentual de aumento: '))
salario_ajustado = ((salario * aumento) / 100) + salario
valor_aumento = (salario * aumento) / 100 # Quero saber o valor do aumento, então calculo o valor do aumento separadamente.

print(f'Com o aumento de {aumento}%, o novo salário será R${salario_ajustado:.2f}')
print(f'O valor do aumento é R${valor_aumento:.2f}')
print('Fim do programa.')



# Exercício 06 - Módulo 1
salario = float(input('Digite o salário do funcionário: R$'))
print(f'O salário do funcionário é R${salario:.2f}')
print(f'O funcionario recebece uma gratificação de 5% do salário, e paga 7% de imposto sobre o salário. ')
salario_ajustado = salario + (salario * 5 / 100) - (salario * 7 / 100) # Esta expressão calcula o valor de um salário após receber um acréscimo de 5% e, em seguida, um desconto de 7% sobre o valor original. Salário + 5% - 7% ordem de precedência soma e depois subtração. 

print(f'O salário a receber é de R${salario_ajustado:.2f}')
print('Fim do programa.')



# Exercício 07 - Módulo 1
salario = float(input('Digite o seu salario: R$'))
salario_gratificado = salario + 600
salario_final = salario_gratificado - (salario * 10 / 100)

print(f'O salário a receber é de R${salario_final:.2f}')
print('Fim do programa.')



# Exercício 08 - Módulo 1
deposito = float(input('Digite o valor do depósito: R$'))
taxa = float(input('Digite a taxa? '))
rendimento = (deposito * taxa) / 100
valor_final = deposito + rendimento

print(f'O valor do rendimento é de R${rendimento:.2f}')
print(f'O valor final é de R${valor_final:.2f}')
print('Fim do programa.')



# Exercício 09 - Módulo 1
print('Este programa calcula a área de um triângulo.')
base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))
area = base * altura / 2

print(f'A área é de {area:.2f}m²')
print('Fim do programa.')



# Exercício 10 - Módulo 1
print('Este programa calcula a área de um círculo.')
raio = float(input('Digite o valor do raio: '))
area = pi * (raio ** 2)

print(f'A área é de {area:.2f}m²')
print('Fim do programa.')



# Exercício 11 - Módulo 1
print('Este programa calcula as horas, minutos e segundos a partir de um valor em segundos.')
segundos_totais = int(input('Digite o tempo em segundos: '))
# 1 hora = 3600 segundos
# 1 minuto = 60 segundos

hora = segundos_totais // 3600
minuto = (segundos_totais % 3600) // 60
segundo = segundos_totais % 60

print(f'{hora} horas, {minuto} minutos e {segundo} segundos')



# Exercício 12 - Módulo 1
print('Este programa emula um caixa eletrônico.')
valor_saque = float(input('Digite o valor que deseja sacar R$'))
cem = int(valor_saque / 100)
valor_saque %= 100
cinq = int(valor_saque / 50)
valor_saque %= 50
vinte = int(valor_saque / 20)
valor_saque %=  20
dez = int(valor_saque / 10)
valor_saque %= 10
cinco = int(valor_saque / 5)
valor_saque %= 5
dois = int(valor_saque / 2)


print(f'Notas de 100: {cem}')
print(f'Notas de 50: {cinq}')  
print(f'Notas de 20: {vinte}')
print(f'Notas de 10: {dez}')
print(f'Notas de 5: {cinco}')
print(f'Notas de 2: {dois}')
print('Fim do programa.')



# Exercício 13 - Módulo 1
print('Digite um número maior que 0 e positivo: ')
numero = int(input('Número: '))

print(f'Número digitado: {numero}')
print(f'Antecessor: {numero - 1}')
print(f'Ao quadrado: {exp2(numero):.2f}')
print(f'Ao cubo: {numero ** 3}')
print(f'Raiz quadrada: {sqrt(numero):.2f}')
print(f'Raiz cúbica: {numero ** (1/3):.2f}')
print('Fim do programa.')



# Exercício 14 - Módulo 1
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
potencia = n1 ** n2

print(f'O resultado de {n1} elevado a {n2} é: {potencia}')



# Exercício 15 - Módulo 1
print('Este programa calcula medida em pes e transforma em polegadas, jardas e milhas.')
# 1 pé = 12 polegadas
# 1 jarda = 3 pés
# 1 milha = 1760 jardas
pes = float(input('Digite a medida em pés: '))
polegadas = pes * 12
jarda = pes / 3
milha = jarda / 1760

print(f'{pes:.2f} pés é equivalente a {polegadas:.2f} polegadas, {jarda:.2f} jardas e {milha:.2f} milhas.')



# Exercício 16 - Módulo 1
nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'A idade é de {idade} anos.')  
print(f'A idade em 2050 será de {2050 - nascimento} anos.')
print('Fim do programa.')

