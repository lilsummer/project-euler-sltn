i = 2
n = 600851475143
result = []
while i**2 <= n:
	if n % i:
		i += 1
	else:
		n = n // i ###n is the floor quotient 
	result = n
print(result)
