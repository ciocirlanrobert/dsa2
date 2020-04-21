For this problem we can use binary search based on the properity of the rotated array. We can see that we basically have two arrays where we can apply the binary search, one from start to middle, and from middle to end.

Complexities:
	=> Time: O(log n) - binary search
	=> Space: O(1)