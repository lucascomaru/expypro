s1 = input('Digite uma string: ')
s2 = input('Digite outra string: ')

tamanho1 = len(s1)
tamanho2 = len(s2)
print(f'{s1} possui {tamanho1} caracteres! ')
print(f'{s2} possui {tamanho2} caracteres! ')
comparando_tamanho = 'diferentes'
comparando_conteudo = 'diferente'
if s1 == s2:
    comparando_tamanho = 'iguais'
    comparando_conteudo = 'igual'
elif tamanho1 == tamanho2:
    comparando_tamanho = 'iguais'
print(f'As duas strings tem tamanhos {comparando_tamanho}')
print(f'As duas strings tem conteudo {comparando_conteudo}')


