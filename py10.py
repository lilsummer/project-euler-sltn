######Find the sum of all the primes below two million.
import numpy as np
set1 = [2,3,5,7,11,13]
pri = []


for i in range(1, 2000000, 2):
	if all(i % item != 0 for item in set1):
		if all(i % item2 != 0 for item2 in pri):
			print(i)
			pri.append(i)
print(np.sum(pri))
print(pri[0:3])