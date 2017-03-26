# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
li = list(range(1, 101, 1))
print(li)

a1 = (sum(li)) ** 2

a2 = 0

for num in li:
	a2 += num ** 2

print(a1 - a2)