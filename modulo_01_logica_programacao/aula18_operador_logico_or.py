# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = 123456

# if (entrada == 'E'or entrada == 'e') and senha_digitada == senha_permitida:
#     print('entrar')
# else:
#     print('sair')

# Avaliação de curto circuito
print(False or 0 or 0 or 'abc' or True)

# tipo avalição numa linha só
senha = input('Senha: ') or 'Sem senha'
print(senha)
