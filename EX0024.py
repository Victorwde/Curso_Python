print('-+'*10,'SIMULAÇÃO DE EMPRÉSTIMO','-+'*10)
valorcasa = float(input('Digite o valor da casa R$: '))
salario = float(input('Informe o seu salário R$:'))
pganos = int(input('Deseja parcelar em quantos anos: '))

valorprest = valorcasa /  (12 * pganos)
novosal = (salario*30/100)
if valorprest < novosal:
    print('Em {:.1f} anos você pagara por mês o valor de R${:.3f} '.format(pganos, valorprest))
else:
    print('O valor da prestação exedeu 30% do seu salário!')
    print('EMPRÉSTIMO NEGADO')