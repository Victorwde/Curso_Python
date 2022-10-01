from ast import Num
import random
from time import sleep
print('Tente acertar o numero escolhido pelo programa !!!')
print('--------------------------------------------------------------')
num = int(input('Digite um numero para jogar: '))
print('Processando...')
sleep(3)
if num == random.randrange(0,5):
    print('PARABENS VOCE É UM GENIO DA ADIVINHAÇÃO')
else:
    print('VOCE NÃO É BURRO, APENAS NÃO ACERTOU O NUMERO')
