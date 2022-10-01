while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('x'*30)
    for i in range(1, 11):
        print(f'O resultado de {i} x {n} é: {i * n}')
    print('x'*30)
print('Programa finalizado.')


