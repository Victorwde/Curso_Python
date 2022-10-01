print('=*=' * 11)
print('=*='*4,'TABUADA','=*='*4)
print('=*=' * 11)
NUM = int(input('Digite um número: '))
for i in range(0, 11):
    result = NUM * i
    print('{} x {} = {}'.format(NUM, i, result))
print('FIM')