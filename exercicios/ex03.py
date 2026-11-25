# Crie um programa que faça comparação de dois numeros
# e mostre na tela, que ou é maior que outro.

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')


if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} e maior ou igual ao {primeiro_valor=} ')
