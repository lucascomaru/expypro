while True:
     try:
         numero = int(input('Digite um número inteiro: '))
     except ValueError:
         print('Deve ser fornecido um valor inteiro')
     else:
        if 0 <= numero <= 10:
             print(f'O número informado é {numero}')
             break
        else:
             print('O número informado deve estar entre 0 e 10')
