import random

r = random.randint(1,100)
count = 0
while True :
	count = count + 1
	rg = input('please guess a number: ')
	rg = int(rg)
	if rg == r:
		print('You are right!')
		print('This is your', count, 'try.')
		break
	elif rg > r:
	    print('Your answer is bigger.') 
	elif rg < r:
		print('Your answer is smaller')
	print('This is your', count, 'try.')
