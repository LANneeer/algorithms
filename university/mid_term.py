"""
Ilik Temirlan IT3-2202
algorithms and data structures mid-term
"""

"""
1,2)
Let A[1, ... n] be an array of distinct numbers. If i < j and A[i] > A[j] then the pair(i, j) is
called an inversion of A.

What is the relationship between the running time of insertion sort and the number of inversions in
the input array?

Answer: If we have "inversion" in n times(our array is reversed) it will have time complexity like n * n
where first `n` is time of running by array and second `n` is time of swapping higher element to the top, so
relationship between running time and "inversions" is n * "inversions"
O(n^2)


Give an algorithm that determines the number of inversions in any permutation on n elements in (n log n)
time complexity
"""

# example array with 14 inversion
my_array = [30, 20, 10, 5, 2, 1]

# example array with 0 inversion
# my_array = [1, 2, 5, 10, 20, 30]


def merge(left: list, right: list, duplicates: int = 0) -> (list, int):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    array = []
    left_index = 0
    right_index = 0

    while len(array) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            array.append(left[left_index])
            left_index += 1
        else:
            duplicates += 1  # is swapped
            array.append(right[right_index])
            right_index += 1

        if right_index == len(right):
            duplicates += 1  # is swapped
            array += left[left_index:]
            break

        if left_index == len(left):
            array += right[right_index:]
            break
    return array, duplicates


def merge_sort(array: list) -> (list, int):
    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2

    left, duplicates_left = merge_sort(array[:mid])
    right, duplicates_right = merge_sort(array[mid:])

    return merge(left=left, right=right, duplicates=duplicates_right+duplicates_left)


print(merge_sort(my_array))


"""
3) Suppose there is a binary min-heap with exactly 6 nodes, containing items with priorities
2,7,9,11,13,15.

Show every possible binary min-heap that could match this description. For each, draw the
appropriate tree and the array representation.

For one of your answers show what would happen if you apply max-heapify once to your
root element.


# min-heaps
        2               2               2               2          
      /   \           /   \           /   \           /   \        
     7     9         9     7         7     9         9     7       
    / \    /        / \    /        / \    /        / \    /    
  11  13  15      11  13  15      13  11  15      13  11  15    

        2               2               2               2         
      /   \           /   \           /   \           /   \       
     7     9         9     7         7     9         9     7      
    / \    /        / \    /        / \    /        / \    /      
  15  13  11      15  13  11      13  15  11      13  15  11     
   
         2               2               2               2         
       /   \           /   \           /   \           /   \       
      7     9         9     7         7     9         9     7      
     / \    /        / \    /        / \    /        / \    /      
   11  15  13      11  15  13      15  11  13      15  11  13      

# max-heapify
        2       =        2       =       11       =       11       =      11      =       15
      /   \     =      /   \     =      /   \     =     /    \     =    /    \    =     /    \    
     7     9    =    11     9    =     2     9    =    13     9    =   13    15   =    13    11   
    / \    /    =   /  \    /    =   /  \    /    =   /  \    /    =  / \    /    =   / \    /    
  11  13  15    =  7   13  15    =  7   13  15    =  7    2  15    = 7   2  9     =  7   2  9     

explanation: 
firstly we sort left side, then we sort right side of left side, and then we repeat this for right sides

# Done
       15
     /    \    
    13    11   
   / \    /    
  7   2  9     
"""


"""
4) Here is an algorithm that is supposed to perform ascending sorting via regular partitions:

Tail-RecursiveQuickSort(A, p, r)
1. while p < r
2.     // Partition and sort left subarray
3.     q = Partition(A, p, r)
4.     Tail-RecursiveQuickSort(A, p, q-1)
5.     p = q + 1

Does it perform correctly? If yes then why?

Answer:

Firstly in Objected oriented programming Languages we have no Tail-Recursion and we will be use
accumulator to transfer result of previous running recursion output to storage like variable
which we declared before run function or allow function to get a parameter like `acc` (mean: accumulator).

If Partition function returns a part of array like {1, 2, 3} it will not works, because it will raise
ArithmeticError when we tries subtract integer from array.

If Partition function returns an value of array, it also will doesn't works, because instance of accumulated
object was not be passed.

Let's see the possible way:
"""

my_array = [90, 20, 45, 10, 5]


def quick_sort(array: list) -> list:
    length = len(array)
    if length <= 1:
        return array

    left, right = [], []
    partition = array[0]
    for item in array[1:]:
        if item <= partition:
            left.append(item)
        if item > partition:
            right.append(item)

    return quick_sort(left) + [partition] + quick_sort(right)


print(quick_sort(my_array))
