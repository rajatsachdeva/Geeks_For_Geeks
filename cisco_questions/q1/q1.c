/* 
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
*/

#include <stdio.h>

int main()
{
	int tc  	= 0;	/* Number of Test cases */
	int n   	= 0;	/* Number of elements in array */
	int sum		= 0;	/* sum from size of array */
	int sum_i	= 0;	/* sum from array entries */
	int curr 	= 0; 	/* Current entry */

	printf("\nEnter number of Test cases: ");
	scanf("%d", &tc);

	while(tc > 0)
	{
		printf("\nTC: %d\nEnter number of elements in array: ", tc-(tc-1));
		scanf("%d", &n);
		sum = (n * (n+1))/2;
		sum_i = 0;

		/* As inputs contains one less entry than array size */
		while(n > 1)
		{
			printf("\nenter value: ");
			scanf("%d", &curr);
			sum_i += curr;
			n--;
		}
		printf("%d\n", sum - sum_i);
		tc--;
	}

	return 0;
}