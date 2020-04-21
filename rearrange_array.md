For this problem I used merge sort in order to sort the array in time O(nlogn). Then, we can easily see that the two numbers with the highest sum, with the difference between the number of digits beign max. 1, are the numbers obtained with the digits from the even indexes, respectively with the digits from the odd indexes. The construction of the number is O(n).

Complexities:
	=>Time : O(nlogn)
	=>Space: O(n) - because of the merge sort