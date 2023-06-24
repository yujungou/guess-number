import random

r = random.randint(1,100)
while True :
	rg = input('please guess a number: ')
	rg = int(rg)
	if rg == r:
		print('You are right!')
		break
	elif rg > r:
	    print('Your answer is bigger.') 
	elif rg < r:
		print('Your answer is smaller')