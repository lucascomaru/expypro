salario_hora = float(input('Quanto vale sua hora? '))
horas_mes = float(input('Quantas horas você trabalha por mes? '))
salario_bruto = salario_hora * horas_mes
inss = (salario_bruto * 8) / 100
ir = (salario_bruto * 11) / 100
sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - inss - ir - sindicato
print(f'Seu salario bruto é {salario_bruto}. O INSS é de : {inss}com IR de {ir}. Para o sindicato:  {sindicato} '
      f' e seu salário final é de : {salario_liquido:.2f}')