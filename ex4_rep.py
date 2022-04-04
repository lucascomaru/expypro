população_pais_a = 80000
população_pais_b = 200000
crescimento_a = 1.03
crescimento_b = 1.015
anos = 0
while população_pais_a < população_pais_b:
        anos+=1
        população_pais_a = int(população_pais_a * crescimento_a)
        população_pais_b *= crescimento_b
        população_pais_b = int(população_pais_b)
print(f'Populações no ano {anos}')
print(f'População A: {população_pais_a}')
print(f'População B: {população_pais_b}')
