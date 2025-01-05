import numpy as np

array = np.array([2, 3, 5, 6, 1, 2, 4])

print("Elements greater than 3:", array[array > 3])

print("Sqr elements:", np.square(array))

avg = np.mean(array)
print("Elements greater than avg:", array[array > avg])

second_array = np.array([1, 2, 1, 2, 1, 2, 3])

print("Element multiplication:", array * second_array)

print("Element division:", array / second_array)

print("Element addition:", array + second_array)
