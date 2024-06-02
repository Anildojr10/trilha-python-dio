# num = 1 

# while(num <= 10):
#     print(num)
#     num += 1
# print('Laço Encerrado')


nome = None

while True:
    print('Digite seu nome, ou X para parar: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo, {nome}')
print('Até Logo!')