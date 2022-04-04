soma = 0
for c in range(1, 6):
    num = int(input(f'Digite o {c} número: '))
    soma+= num
    media = soma/5
    print(f'A soma dos números é {soma} e a média é {media}')