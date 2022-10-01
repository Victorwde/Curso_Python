print('=*=' * 11)
print(' '*4,'10 TERMOS DE UMA PA',' '*4)
print('=*=' * 11)
pri = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = pri + (10 - 1) * razão
for i in range(pri, décimo + razão, razão):
    print('{}'.format(i), end=' -> ')
print('ACABOU')
