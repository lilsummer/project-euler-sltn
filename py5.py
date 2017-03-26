# what is the smallest number that is evenly disivle by all of the numbers from 1 to 20

# i = 10135770
# li  = list(range(10,21))
# # print(li)
# while True:
# 	j = [i % num for num in li]
# 	print(j)
# 	if sum(j) == 0:
# 		print("result:" + str(i))
# 		break
# 	else:
# 		i += 1
# 		print(i)

######################### not using recurision ###############
####################### not using recursion ############
li = list(range(11,21))
print(li)
result = 0
for i in range(2520,99999999999, 2520):  ##change to range(1, 999999999, 2520) the program will slow down
	if all(i % num == 0 for num in li):
		print(i)
		result = i
		break

print(result)