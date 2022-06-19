Insertion Sort 
==========================
- Definition  
  It's a way to change positions only when necessary.
-----------------------------
<pre>
<code>
#include <stdio.h>

int main(void) {
	int i, j, temp;
	int array[10] = { 1,10,5,8,7,6,4,3,2,9 };
	for (i = 0; i < 9; i++) {
		j = i;
		while (array[j] > array[j + 1]) {  //Change positions only when necessary
			temp = array[j];
			array[j] = array[j + 1];     //swap
			array[j + 1] = temp;
			j--;
		}
	}
	for (i = 0; i < 10; i++) {
		printf("%d ", array[i]);
	}
	return 0;
}

</code>
</pre>

- big-O notation  
  n=(n+1)/2  => O(n^2)

It's very fast when it's almost aligned. It's faster than selection sort and bubble sort.
