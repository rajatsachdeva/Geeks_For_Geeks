tc = int(input("Enter number of TC's: "))
sum_i = 0
for i in range(tc):
	print("TEST CASE {}".format(i+1))
	n 		= int(input("Enter size of array:"))
	sum_n 	= int((n * (n + 1))/2)
	print("Sum_n is {}".format(sum_n))
	sum_i	= 0
	l = input().split()
	results = list(map(int, l))	
	print (l, type(l))
	print (results, type(results))
	sum_i = int(sum(results))
	print(sum_n - sum_i) 
