# Getting familiar with NumPy.

## Numpy vs Python Lists.

Numpy provides powerful and faster computation tools to work with n-dimensional array.
This is possible due to the use of vectorized code. Code that are written in C language which are pre-compiled and are faster that are written to work on whole array.
Python lists needs loops to work on each element where as Numpy works on whole arrays.

Another difference is in there types, Python list can hold multiple data types whereas Numpy holds elements of same type only.

check Activity 1 and 2 for examples.

### Basics:

- np.array([1,2]) to create 1-d array like wise np.array([[1,2],[3,4]]) for 2-d and follow like wise to create n-d array.
- shape : tells the number of rows and arrays of the array.
- dtype : tells you the data type of the array
- broadcasting: np.array([1,2]) * 2 can be done this will multiply all the elements by 2.
- easy to use statistical methods like, min(np.array([1,2,3,4])) gives the average of this array, max



### Working with 2d array
**Note: scores is a 2d array**
**where axis is 0 = column and 1 = row**

- np.mean(scores, axis=1) this is used to find the average per row or per column based on the axis. The return is an array.
- np argmax(scores,axis=1) returns the index of the max from the array.

## slicing
select a range of elements.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr[:, 1] here it selects all the rows and only 1th index column
the print would be [2,5,8]
