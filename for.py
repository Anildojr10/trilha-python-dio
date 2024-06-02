# lista = [2, 6, 9, 4, 0, 12, 3, 7 ]

# for item in lista:
#     print(item)

# palavra = 'Anildo'

# for letra in palavra:
#     print(letra)

# for numero in range(1,11):
#     print(numero)


# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)
# for x in range(2,20):
#     print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safíra', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)