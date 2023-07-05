import numpy as np

a = np.array([1, 2, 3])

print(a)


b = np.array([["A", "D", "G"], ["B", "E", "H"], ["C", "F", "I"]])
print(b)


print("\nDimension of Array A = ",a.ndim)
print("\nDimension of Array B = ",b.ndim)

print("\nShape of Array A = ",a.shape)
print("\nShape of Array B = ",b.shape)

print("\nSize of Array A = ",a.size)
print("\nSize of Array B = ",b.size)

print("\nItem Size of Array A = ",a.itemsize)
print("\nItem Size of Array B = ",b.itemsize)

print("\nData Type of Array A = ",a.dtype)
print("\nData Type of Array B = ",b.dtype)

