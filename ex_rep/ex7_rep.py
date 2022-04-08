num = float(input('Digite um número: '))
for _ in range(4):
    num = max(num, float(input('Digite um número: ')))
    print(f'O maior número encontrado foi {num}')
