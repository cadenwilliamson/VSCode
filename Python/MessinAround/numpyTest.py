from numpy import array
from operator import concat

python_array = [1,2,3,4,5]
numpy_array = array([1,2,3,4,5])

print(python_array, "\n")
print(numpy_array, "\n")


a = array([[1,2], [3,4]])
b = array([[5,6], [7,8]])

ab = a + b

print(a, "\n")
print(b, "\n")
print(ab, "\n")