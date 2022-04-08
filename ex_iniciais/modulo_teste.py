menor = maior =qnt = 0
for c in range(1, 6):
    idade = int(input(f'Digite a {c} idade: '))
    qnt+=1
    if qnt ==1:
        maior = menor = idade
    else:
        if idade > maior:
           maior = idade
        if idade < menor:
           menor = idade
print(f'Você digitou {qnt} idades')
print(f'A maior idade é : {maior}')
print(f'A menor idade é : {menor}')


