def handle_input(inpt):
	inpt = inpt.split(" ")
	x = int(inpt[0])
	y = int(inpt[1])
	return x, y


def printshit(all_ML):
	reversed_list = list()
	for i in range(len(all_ML)):
		reversed_list.append(all_ML.pop())
	for j in range(len(reversed_list)):
		print(reversed_list[j])
def prob(n,m):
	max_value = n+m
	cntlist = [0]*max_value
	for i in range(n):
		for j in range(m):
			cntlist[i+j] = cntlist[i+j] + 1
	if (n == m):
		most_likely = max(cntlist)
		most_likely = cntlist.index(most_likely)
		most_likely = max_value-most_likely
		print(most_likely)
	else:
		most_likely = max(cntlist)
		#print("most", most_likely)
		all_ML = list()
		#print(cntlist)
		for k in range(m+n):
			if cntlist[k] == most_likely:
				iindex = cntlist.index(most_likely)
				cntlist[k] = 0
				#print("iindex",iindex)
				all_ML.append(iindex)
		for p in range(len(all_ML)):
			all_ML[p] = (n+m)- all_ML[p]

		printshit(all_ML)
	#print(most_likely)
	#print(cntlist)

inpt = input()
n, m = handle_input(inpt)
prob(n, m)