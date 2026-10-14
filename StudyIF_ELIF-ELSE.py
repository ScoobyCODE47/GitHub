from random import randint
from time import sleep

num = randint(1, 10)
print('O computador escolherá um número de 1 a 10, cada número corresponde a um dia na semana. Qual será o número escolhido? ')
sleep(4)
print(f'O número escolhido foi: {num}')
sleep(2)

if num == 1:
    print(f'O número {num}, corresponde a DOMINGO.')

elif num == 2:
    print(f'O número {num}, corresponde a Segunda-Feira.')

elif num == 3:
    print(f'O número {num}, corresponde a Terça-Feira.')

elif num == 4:
    print(f'O número {num}, corresponde a Quarta-Feira.')

elif num == 5:
    print(f'O número {num}, corresponde a Quinta-Feira.')

elif num == 6:
    print(f'O número {num}, corresponde a Sexta-Feira.')

elif num == 7:
    print(f'O número {num}, corresponde a Sábado.')

else:
    print('Número inválido!')

print('Fim do programa!')
print('Obrigado por participar!')
