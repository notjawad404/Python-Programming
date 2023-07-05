import numpy as np

arr1 = np.zeros((3, 4), dtype=np.int16)  # 0 is the value to be filled


print("Array 1 \n",arr1)

arr2 = np.ones((3, 4), dtype=np.int16)   # 1 is the value to be filled
print("\nArray 2 \n",arr2)

arr3 = np.full((3, 4), 5, dtype=np.int16)   # 5 is the value to be filled   
print("\nArray 3 \n",arr3)

r1 = np.random.random((3, 4))       # Random number between 0 and 1
print("\nRandom Array 1 \n",r1)

r2 = np.random.randint(1, 10, (3, 4))     # Random number between 1 and 10
print("\nRandom Array 2 \n",r2)

range1 = np.arange(1, 10, 2)    # start, stop, step
print("\nRange Array 1 \n",range1)

range2 = np.arange(1, 10)  # start, stop
print("\nRange Array 2 \n",range2)

lineSpace1 = np.linspace(1, 10, 5)  # start, stop, number of elements
print("\nLine Space Array 1 \n",lineSpace1)

reshape1 = np.arange(1, 10).reshape(3, 3)  # start, stop, and reshape
print("\nReshape Array 1 \n",reshape1)

ravel1 = np.ravel(reshape1)  # start, stop, and reshape
print("\nRavel Array 1 \n",ravel1)

array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

min1 = array1.min()
print("\nMinimum Value of Array 1 = ",min1)

min2 = array1.min(axis=0)
print("\nMinimum Value of Array 1 = ",min2)

max1 = array1.max()
print("\nMaximum Value of Array 1 = ",max1)

max2 = array1.max(axis=0)
print("\nMaximum Value of Array 1 = ",max2)

sqrt1 = np.sqrt(array1)
print("\nSquare Root of Array 1 = \n",sqrt1)

std1 = np.std(array1)
print("\nStandard Deviation of Array 1 = ",std1)

