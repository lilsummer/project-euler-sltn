
#######Find the sum of all the primes below two million.
import numpy as np
###  sieve of Eratosthenes
def eratosthenes(n):
    P = [i for i in range(2, n+1)]
    p = 0
    while True:
        for i in P[p + 1:]:
            if i % P[p] == 0:
                P.remove(i)
        if P[p]**2 >= P[-1]:
            break
        p += 1
    return P

result = eratosthenes(2000000)

### 
scan = list(range(3, 20000,2))
set1 = [2,3,5,7,11,13,19]
print(len(scan))
print(len(set1))
for i in scan:
    if any(i % num == 0 for num in set1):
        set1.append(i)
        scan.remove(i)
        
print(len(scan))
print(len(set1))


## set1 is the multiple of prime numbers
##I am done fuck