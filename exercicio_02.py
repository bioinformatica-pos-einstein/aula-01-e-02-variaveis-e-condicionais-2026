numero = int(input('Digite um número: '))
print(f"""Resposta:
O antecessor do número {numero} é {numero - 1}.
O sucessor do número {numero} é {numero + 1}.
O dobro do número {numero} é {numero * 2}.
A raiz quadrada do número {numero} é {format(numero ** 0.5, '.2f')}.""")