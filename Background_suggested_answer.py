import numpy as np

#Create a simple numpy array
array = np.array ( [[ 1, 2, 3, 4 ],
                    [ 5, 6, 7, 8 ]] )


#Find the attributes of the simple array
print ("----------------The simple array-----------------------------")
print ("The number of axes:", array.ndim)
print ("Dimensions of the array:", array.shape)
print ("Total number of elements:", array.size)
print ("The type of elements:", array.dtype)


#Now we create a slightly more complex numpy array
complex_array = np.array ( [[[ 1, 2 ], [3, 4.5]],
                            [[ 5, 6 ], [7, 8]],
                            [[ 9, 10], [11, 12]]] )


#Delete the """ to uncomment this part
#Replace all ##replaceme## until all four results are true

print ()
print ("----------------The complex array-----------------------------")
print ( complex_array.ndim == 3 )
print (complex_array.shape == (3, 2, 2) )
print (complex_array.size == 12 )
print (complex_array.dtype == "float64" ) #this is a string

