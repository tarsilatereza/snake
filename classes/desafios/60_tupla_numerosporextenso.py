cont = ('zero', 'um', 'dois', 'três', 'quatro', 
	'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
	num = int(input('digite um número entre 0 e 10: '))
	if 0 <= num <= 20:
		break
	print('tente novamente. ', end='')
print(f'você digitou o número {cont[num]}')