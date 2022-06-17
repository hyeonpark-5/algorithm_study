Selection Sort 
==========================
- Definition  
  The algorithm that selects the smallest one and sends it to the front.
-----------------------------
<pre>
<code>
#include <stdio.h>
int main(void) {

	int i, j, min, index, temp;
	int array[10] = { 1,10,5,8,7,6,4,3,2,9 };
	for (i = 0; i < 10; i++) {

		min = 9999;
		for (j = i; j < 10; j++) {     //Nested loop, minimum
			if (min > array[j]) {
				min = array[j];
				index = j;
			}
		}

		temp = array[i];               //swap
		array[i] = array[index];
		array[index] = temp;
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
