# Python_A2_G11
Python course Assignment 2 done by group 11 - Ankur, Mahika, Amar, Ritvik

Comparison of time complexities b/w sorting- Bubble and Merge sort, and, searching- Linear and Binary search algorithms.

Bubble Sort: simplest sorting algo that works by repeatedly swapping the adjacent elements if they are not in the required order.
    _Time Complexity: O(N^2)_
    _Space Complexity: O(1)_

Merge Sort: is a divide and conquer algo, works by dividing the input array iin two halves, and calls itself for the two halves and then merges the two sorted halves.
    _Time Complexity: O(N*log(N))_
    _Space Complexity: O(N)_

Linear Search: a sequential manner is used to find the required element. Every element is checked about the value we're searching. If both are equal, then the element is found and the  process returns that element's index position.
    _Time Complexity: O(N)_
    _Space Complexity: for iterative:- O(1); for recursive:- O(N)_

Binary Search: used to search an element in a sorted array. It's an efficient algorithm and is better than linear search in terms of time complexity.
    _Time Complexity: O(log N)_
    _Space Complexity: O(log N)_

**It's expected that Merge Sort is the better one when compared to Bubble Sort in normal and worst case scenarios.**
**It's also expected that Binary Search is going to be better than Linear Search(when using sorted data) in normal and worst case scenarios, as when there is unsorted data Binary Search cannot be applied.**
