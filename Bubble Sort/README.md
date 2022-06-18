Bubble Sort 
==========================
- Definition  
  It is a method of sending a smaller value forward compared to the value next to it.
-----------------------------
<pre>
<code>
#include<stdio.h>

int main(void) {
	int i, j, temp;
	int array[10] = { 1,10,5,8,7,6,4,3,2,9 };
	for (i = 0; i < 10; i++) {
		for (j = 0; j < 9 - i; j++) {        //Nested loop, swap
			if (array[j] > array[j + 1]) {
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}
	return 0;
}

</code>
</pre>

- big-O notation  
  n=(n+1)/2  => O(n^2)

The efficiency is the worst among the sorting algorithms. This is because of the repeated swaps.
