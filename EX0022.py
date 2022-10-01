print('==============Viagem ou Viajem=================')
km = int(input('Quantos KMs voce vai viajar: '))
if km <= 200:
    valor = 0.50 * km
    print('Sua viagem vai custar R${}'.format(valor))
else:
    valor2 = 0.45 * km
    print('Sua viagem vai custar R${}'.format(valor2))