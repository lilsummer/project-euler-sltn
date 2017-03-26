# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?
pri = []

set1 = [2,3,5,7,11,13]

for num in range(2, 99999999):
	if len(pri) < 10001 - 6:
		if any(num % i == 0 for i in set1):	
			pri = pri
		elif any(num % i == 0 for i in pri):
			pri = pri
		else:
			pri.append(num)
	else:
		break

print(pri[len(pri)-1])
print(len(pri))
print(pri[0:10])