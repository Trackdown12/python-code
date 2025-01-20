import numpy as np

#a=np.array([[1,2,3],
#           [4,"Hello",6],
#          [7,8,9]],dtype=np.int32)
#this will provide error as it is not possible to convert string to int32


a=np.array([[1,2,3],
           [4,"5",6],
          [7,8,9]],dtype=np.int32)
print(f"printing data type={a.dtype}")
#this will be executed as string 5 can be conberted into integer data type

d={1:"a",2:"b",3:"c"}
arraydict=np.array([[1,2,3,d],
                    [4,{1:2,3:4},6,7]])
print(f"printing array with dictionary={arraydict}")
print(f"printing data type of array with dictionary={arraydict.dtype}")#output=object
print(f"printing shape of array with dictionary={arraydict.shape}")#output=(2,4) as it contains to rows and four columns


#===============there is a difference between <class 'int'> and <class 'numpy.int32'>================



#creating an array full of same number
ar=np.full((3,3),5)#(3,3) is shape of array and 5 is number which will be filled in array
print(f"printing array full of 5={ar}")
#3d array basically create a 3d array with 3 rows,3 columns and 3 depth meanwhile 4d array will create a 4d array with 3 rows,3 columns,3 depth and 3 height


ar2=np.full((3,3,3,3),5)
print(f"printing 4d array full of 5={ar2}")




#============mathematics difference between numpy array and list================
l1=[1,2,3,4]
l2=[5,6,7,8]

ar=np.array(l1)
ar2=np.array(l2)

#now if we add two lists it will concatenate them
print(f"adding two lists={l1+l2}")#output=[1,2,3,4,5,6,7,8]
#but if we add two numpy arrays it will add them element wise like a addition in matrix
print(f"adding two numpy arrays={ar+ar2}")#output=[6 8 10 12]

#similarly if we subtract two lists it will give error
#but if we subtract two numpy arrays it will subtract them element wise like a subtraction in matrix
print(f"subtracting two numpy arrays={ar2-ar}")#output=[4 4 4 4]

#similarly if we multiply two lists it will give error
#but if we multiply two numpy arrays it will multiply with the corresponding elements
print(f"multiplying two numpy arrays={ar2*ar}")#output=[5 12 21 32]

#similarly if we divide two lists it will give error
#but if we divide two numpy arrays it will divide them with the correspomnding elements
print(f"dividing two numpy arrays={ar2/ar}")#output=[5. 3. 2.33333333 2.]

#for doing matrix multiplication we use dot function
print(f"matrix multiplication of two numpy arrays={np.dot(ar2,ar)}")#output=70
print("this method too provide matrix multiplication",ar@ar2)#output=70