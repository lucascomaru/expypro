numero = int(input('Digite um número inteiro de 0 a 999: '))
centena_Str = dezena_str = unidade_str = ''
centena_int, numero = divmod(numero, 100)
partes_numericas = 0
#Tratando singular e plural
if centena_int == 1:
    centena_Str = '1 centena'
    partes_numericas += 1
elif centena_int > 1:
    centena_Str = f'{centena_int} centenas'
    partes_numericas += 1
dezenas_int, numero = divmod(numero, 10)
if dezenas_int == 1:
    dezena_str = '1 dezena'
    partes_numericas += 1
elif dezenas_int >1:
    dezena_str = f'{dezenas_int} dezenas'
    partes_numericas += 1
if numero == 1:
    unidade_str = '1 unidade'
    partes_numericas += 1
elif numero >1:
    unidade_str = f'{numero} unidades'
    partes_numericas += 1
#Formatando o código!
if partes_numericas == 0:
    print('Número 0 não possui centenas,dezenas ou unidades')
elif partes_numericas == 1:
    print(centena_Str + dezena_str + unidade_str)
elif partes_numericas == 3:
    print(f'{centena_Str}, {dezena_str}, {unidade_str}')
elif partes_numericas == 2:
    if centena_Str != '':
        segunda_parte = dezena_str + unidade_str
        print(f'{centena_Str} e {segunda_parte}')
    else:
        print(f'{dezena_str} e {unidade_str}')