import numpy as np
a=np.array([1,2,3,4],dtype=complex)#provides complex number as output [1. +0.j 2. +0.j 3. +0.j 4. +0.j]
print("printing complex array=",a)
print("checking data type of array",a.dtype)#----complex128---
a=np.array([5,6,7,8])#creating simple array of integers
l=[1,2,3,4]#creating simple list
print("printing list",l)#output = [1,2,3,4]
print("printing array",a)#output = [1 2 3 4]
print("subtracting list from array which we give output in array=",a-l)#output = [4 4 4 4]
print("checking type of array=",type(a))#----<class 'numpy.ndarray'>---
print("checking data type of array=",a.dtype)#----int32---
print("printing element at index 1=",a[1])#output=6
print("printing sliced array from index 1 to end=",a[1:])#output=[6 7 8]
print("dimension of array=",a.ndim)#output=1----->dimension of array for example 1d,2d,3d  [ndim represents number of dimensions]
a[1]=5.5
print("printing array after  trying to insert a float value 5.5 at index 1 but output will be 5 as array is integer based by default when created based on the elements inserted it will give output 5 after truncation=",a)#output=[5 5 7 8]



b=np.array(l)#passing list as argument in array function
print(f"printing array b which is created by passing list as argument in array function={b}")#output=[1 2 3 4]

#c=np.array()     #TypeError: array() missing required argument 'object' (pos 0)
#c[0]=1
#print(c)


'''------------2d array-----------------'''
array_2d=np.array([[1,2],
                   [4,5],
                   [7,8]])
print(f"printing 2d array={array_2d}")#output=[[1 2][4 5][7 8]]
print(f"printing [1,1]element of 2d array={array_2d[1,1]}")#output=5  --->row 1 and column 1
print(f"printing 2nd row {array_2d[1]}----indexing starts from 0 so for printing n'th row requires argument n-1---- ")#output=[4,5,6]
print(f'array shape ={array_2d.shape}')#output=(3,3) three columns and three rows
print(f'array dimension={array_2d.ndim}')#output=2    ------>dimension of array for example 1d,2d,3d  [ndim represents number of dimensions]
print(f"total elements={array_2d.size}")#output=9    ----->total number of elements in array(basically rows*columns)
print(f"dataype={array_2d.dtype}")#output=int32 ----->data type of array
print(f"array size in bit={array_2d.itemsize}")#output=4 ----->size of each element in array in bytes


array2nd_2d=np.array([[1,2,3],
                      [7,8,9],
                      [4,5,6]],dtype=np.int64)
print(f"dtype of multidimensional array after setting it to int64 meaning 64 bit architecture={array2nd_2d.dtype}")#output=int64

'''=======above some lines show that datatype(dtype) is set to int32 as default based on size array is taking place in memory'''




"""===========3d array=================="""
array3d=np.array([[[1,2,3],[1,2,3],[1,2,3]],
                    [[4,5,6],[4,5,6],[4,5,6]],
                    [[7,8,9],[7,8,9],[7,8,9]]])
print(f"printing 1st 3d array={array3d}")
print(f"printing 1st 3d array shape={array3d.shape}")#output=(3,3,3) 3 rows,3 columns and 3 depth
print(f'number of dimensions={array3d.ndim}')#output=3    ------>dimension of array for example 1d,2d,3d  [ndim represents number of dimensions]


array2nd_3d=np.array([[[1,2],[1,2],[1,2]],
                    [[4,5],[4,5],[4,5]],
                    [[7,8],[7,8],[7,8]]])
print(f"printing 2nd 3d array={array2nd_3d}")
print(f"printing 2nd 3d array shape={array2nd_3d.shape}")#output=(3,3,2) 3 rows,3 columns and 2 depth
print("printing index 0,0,1=",array2nd_3d[0][0][1])#output=2
print("printing type of element atindex 0,0,1=",type(array2nd_3d[0][0][1]))#output=<class 'numpy.int32'>

