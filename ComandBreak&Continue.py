for i in range(1, 11, 1):
    if i == 5:
        continue # O comando irá ignorar a 5º situação.
    print(f'{i}º situação')
    
print('Fim do programa!')



for i in range(1, 10, 1):
    if i == 5:
        break # O comando irá interromper na 5º posição
    print(f'{i}º situação')

print('Fim do programa!')



# Desafio
contador = 0

while True:
    print(f'Contador {contador}')
    escolha = input('Deseja incrementar o contador? (S/N)? ')

    if escolha == 's':
        contador += 1
        continue

    if escolha == 'n':
        print('Fim do programa!')
        break
