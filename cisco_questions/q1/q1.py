'''
Given an array of size n-1 and given that there are numbers from 1 to n with 
one missing, the missing number is to be found.

Input:

The first line of input contains an integer T denoting the number of test cases
The first line of each test case is N.
The second line of each test case contains N-1 input C[i],numbers in array.

Output:

Print the missing number in array.

Constraints:

1 ≤ T ≤ 200
1 ≤ N ≤ 1000
1 ≤ C[i] ≤ 1000

Example:

Input
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output
4
9
'''
#Code
sum_n 	= 0
sum_i	= 0
n 		= 0
tc = int(input())
for i in range(tc):
    #print("TEST CASE {}".format(i+1))
    n       = int(input())
    sum_n   = int((n * (n + 1))/2)
    #print("Sum_n is {}".format(sum_n))
    sum_i   = 0
    l = input().split()
    results = list(map(int, l))
    #print (l, type(l))
    #print (results, type(results))
    sum_i = int(sum(results))
    print(sum_n - sum_i)