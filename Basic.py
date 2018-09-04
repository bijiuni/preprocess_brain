import numpy as np

#Task 1
#We define an array1
array1 = np.array ( [[1., 1., 1.],
                     [1., 1., 1.]], dtype=int)
#Use ones function to define array_ones so that it is equal to array1
array_ones = 1
#Make this true
print (np.array_equal(array_ones, array1) )


#Task 2
#We define an array2
array2 = np.array ( [0, 2, 4, 6, 8] )
#Use arange function to define array_arange so that it is equal to array2
array_arange = 1
#Make this true
print (np.array_equal(array_arange, array2) )


#Task 3
#We define an array3
array3 = np.array ( [0, 0.25, 0.5, 0.75, 1] )
#Use linspace function to define array_linspace so that it is equal to array3
array_linspace = 1
#Make this true
print (np.array_equal(array_linspace, array3) )


#Task 4
#Before uncommenting and running these, think about what the results will be
"""
print ("--------------simple operations----------------------")
print (array2 * 5)
print (array2 / 2)
print (array2 ** 2)
print (array2 <= 5)

print ("----------------upcasting---------------------------")
array4 = array2 + array3
print (array4)
print (array4.dtype)
"""

#Task 5
#Which of the following demand will not generate errors?
#Uncomment that one
#print ("------------------multiplication---------------------")
array1 = np.array ( [[1., 1., 1.],
                     [1., 1., 1.]], dtype=int)
array5 = np.array( [[1, 2],
                    [3, 4],
                    [5, 6]] )
#print (array1 * array5)
#print (np.dot (array1, array5) )
