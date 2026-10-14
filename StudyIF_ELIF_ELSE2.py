from random import randint 
from time import sleep

print('O computador vai escolher um número de 1 a 15, cada número corresponde ao nome do mês no calendário. Caso o número for diferente, ira aparecer "invalido". ')
sleep(4)

print('Qual será o número escolhido? ')
num = randint(1, 15)

sleep(2)
print(f'O número escolhido foi: {num}')

sleep(2)

if num == 1:
    print(f'O número {num}, corresponde a Janeiro.')

elif num == 2:
    print(f'O número {num}, corresponde a Fevereiro.')

elif num == 3:
    print(f'O número {num}, corresponde a Março.')

elif num == 4:
    print(f'O número {num}, corresponde a Abriu.')

elif num == 5:
    print(f'O número {num}, corresponde a Maio.')

elif num == 6:
    print(f'O número {num}, corresponde a Junho.')

elif num == 7:
    print(f'O número {num}, corresponde a Julho.')

elif num == 8:
    print(f'O número {num}, corresponde a Agosto.')

elif num == 9:
    print(f'O número {num}, corresponde a Setembro.')

elif num == 10:
    print(f'O número {num}, corresponde a Outubro.')

elif num == 11:
    print(f'O número {num}, corresponde a Novembro.')

elif num == 12:
    print(f'O número {num}, corresponde a Dezembro.')

else:
    print('Número Invalido!')

print('Fim do Programa!')
