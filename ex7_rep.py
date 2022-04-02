maior = 0
for c in range(1,6):
    numero = int(input('Digite um número inteiro: '))
    if numero > maior:
        maior = numero
print(f'O maior número é {maior}')
