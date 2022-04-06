def imprimir_triangulo_de_numeros_crescentes(n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end= '   ')
        print('')

print('Triângulo com 1')
imprimir_triangulo_de_numeros_crescentes(1)
print('Triângulo com 2')
imprimir_triangulo_de_numeros_crescentes(2)
print('Triângulo com 3')
imprimir_triangulo_de_numeros_crescentes(3)