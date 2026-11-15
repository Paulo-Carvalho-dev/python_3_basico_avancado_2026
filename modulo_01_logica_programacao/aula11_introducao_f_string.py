nome = 'Paulo Carvalho'
altura = 1.80
peso = 97.4
imc = peso / altura ** 2

# Fomatando texto com f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
