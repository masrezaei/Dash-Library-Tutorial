# ----------- Numpy Basic -------------
import numpy as np

my_list = [0,1,2,3,4]
arr = np.array(my_list)
print(arr)

# arange function (start,stop,step)
a = np.arange(0,10)
b= np.arange(0,10,2)

# Create an array of zeros and ones
c = np.zeros((5,5))
d = np.ones((2,4))

# Create an array of random integers (uniform distribution between limits)
e = np.random.randint(0,10)
# Create 2d matrix of random ints
f = np.random.randint(0,10,(3,3))

# Create linearly spaced array
g = np.linspace(0,10,6)
h = np.linspace(0,10,101)
print(a)

# ----------- Numpy Operations -------------
# Setting a seed allows you to get the same "random" numbers that we do
np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)

# Simple operations
print(arr.max())
print(arr.min())
print(arr.mean())
# Index location of min
print(arr.argmin())
print(arr.argmax())
print(arr.reshape(2,5))

# ----------- Indexing -------------
mat = np.arange(0,100).reshape(10,10)
row = 0
col = 1
print(mat[row,col])   # Selecting an individual number:
print(mat[:,col])   # Select an entire column 
print(mat[row,:])    # Select an entire column

# ----------- Masking -------------
# Masking allows you to use conditional filters to grab elements
print(mat > 50)
print(mat[mat>50])

