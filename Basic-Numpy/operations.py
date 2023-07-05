# Operations in Array:
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nArray 1 + Array 2\n",arr1 + arr2)

print("\nArray 1 - Array 2\n",arr1 - arr2)

print("\nArray 1 * Array 2\n",arr1 * arr2)

print("\nArray 1 / Array 2\n",arr1 / arr2)

print("\nArray 1 % Array 2\n",arr1 % arr2)

print("\nMatrix dot product\n",arr1.dot(arr2))