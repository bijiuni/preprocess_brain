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
"""
print ()
print ("----------------The complex array-----------------------------")
print ( complex_array.ndim == ##replaceme## )
print (complex_array.shape == ##replaceme## )
print (complex_array.size == ##replaceme## )
print (complex_array.dtype == ##replaceme## ) #this is a string
"""
