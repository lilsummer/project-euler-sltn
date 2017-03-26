# largest palindromic product made by 3 digit numbers

a = 999
###########################################
# this is a smart recursion program
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
############################################


####### this is an iteration ##################
pro = []
for i in range(999, 1, -1):
	for j in range(999, 1, -1):
		lens = len(str(i*j))
		mid = int(lens/2)
		first = str(i*j)[0 : mid]
		second = reverse(str(i*j)[mid:])
		#print(first + second)
		if first == second:
			pro.append(i*j)

pro = sorted(pro)
print(pro[len(pro)-1])
