import numpy as np
a=np.array([1,2,3])
print(f"array at the start:{a}")
#==syntax to insert multiple elements in 1d array===
a=np.insert(a,3,[5,6,7])#inserting [5,6,7] at index 3 which will insert the elements only not array
print(f"appending  multiple element:{a}")

#==syntax to insert single elements in 1d array===
a=np.insert(a,3,4)#array,index,element in argument
print(f"appending 4 at index 3:{a}")

#==syntax to append multiple elements in 1d array===
a=np.append(a,[8,9,10])#appending [8,9,10] at the end of array
print(f"appending multiple element:{a}")

#syntax to insert single element in 1d array==
a=np.append(a,11)#appending 11 at the end of array
print(f"appending 11:{a}")

a=np.delete(a,3)#deleting element at index 3
print(f"deleting at index 3:{a}")


#=============reshaping of array================

"""
note:->reshaping of array is done to change the shape of array without changing the data of array
        this can be done by using reshape() function
        *syntax:->arrayname.reshape(row,column)
        number of elements in array should be equal to row*column
        so the reshaping should not alter number of elements
"""

b=np.array([[1,2,3,4],
            [5,6,7,8]])
#above array has 2 rows and 4 columns
#total 8 elements which means it can be reshaped as 2*2*2,4*2,2*4,8*1 and 1*8
print(f"reshaping of array (4,2)={b.reshape(4,2)} \n")#4rows 2 columns
print(f"reshaping of array (2,4)={b.reshape(2,4)}\n")#2rows 4 columns
print(f"reshaping of array (8,1)={b.reshape(8,1)}\n")#8rows 1 column
print(f"reshaping of array (1,8)={b.reshape(1,8)}\n")#1rows 8 columns
print(f"reshaping of array (2,2,2)={b.reshape(2,2,2)}\n")#2rows 2 columns 2 depth

#array.reshape returns the array which means it should be stored to take place in original array
#example
print(b)#output=[[1 2 3 4] [5 6 7 8]] still o/p not changed


#to actually reshape array in original array we should use array.resize
b.resize(4,2)
print(b)#output=[[1 2] [3 4] [5 6] [7 8]] output has been changed


"""
difference btw reshape and resize is that reshape returns the reshaped array but resize changes the original array    
"""


# flatten and ravel
#flatten and ravel are used to convert multi dimensional array into 1d array
#flatten returns the copy of original array while ravel returns the view of original array
#example
c=np.array([[1,2,3,4],
            [5,6,7,8]])
v=c.flatten()
print(f"flatten array before changiong element={v}")#output=[1 2 3 4 5 6 7 8]
v[2]=9
print(f"flattenarray after changiong element={v}")#output=[1 2 9 4 5 6 7 8]
print(f"original array={c}")#output=[[1 2 3 4] [5 6 7 8]] so the original array is not changed

#example of ravel
v1=c.ravel()
print(f"ravel array before changiong element={v1}")#output=[1 2 3 4 5 6 7 8]
v1[2]=9
print(f"ravel array after changiong element={v1}")#output=[1 2 9 4 5 6 7 8]
print(f"original array={c}")#output=[[1 2 9 4] [5 6 7 8]] so the original array is changed
#here you can see when we change something in ravel array it changes the original array as well because ravel returns the view of original array


#transpose of matrix
d=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print("matrix before transpose",d)
d=d.transpose()#d.T can also be used for transpose
print("matrix after transpose",d)
d=d.T
print("matrix after second transpose(second transpose refers to original array)",d)