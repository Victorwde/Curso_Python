medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.2f}cm e {:.2f}mm'.format(medida, cm, mm))