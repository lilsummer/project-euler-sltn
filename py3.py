# What is the largest prime factor of the number 600851475143 ?
import math
num = 600851475142
while True:
	print(num)
	if num % 2 == 0: # is even number
		num -= 1
	elif num % 3 == 0:
		num -= 1
	elif num % 5 == 0:
		num -= 1
	else:
		if 600851475143 % num == 0:
			print(num)
			break
		else:
			num -= 1



