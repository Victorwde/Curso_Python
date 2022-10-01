print('---------------RADAR---------------')
veloci = int(input('Velocidade do veiculo: '))
if veloci > 80:
    multa = veloci - 80
    multa = 7 * multa
    print('VOCE FOI MULTADO E TERA QUE PAGAR R${}'.format(multa))
else:
    print('OK voce esta dentro do limite de velocidade ')