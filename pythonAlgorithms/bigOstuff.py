
'''
algorithms work on data sets and solve computational problems, so it is important
to understand algorithm performance. Understanding performance helps you to choose
an algorithm to solve a problem and tells you what to expect from your program under
different circumstances.

Big-O notation tells how an algorithm performs as the size of the input data set
grows over time (the growth rate of an algorithm's time complexity is referred to as
the 'order of operations' thus the 'O' in Big-O). Many algorithms and data structures
have more than one Big-O value.

Big-O short list:

Notation        Description        Example
--------------------------------------------------------
O(1)            Constant time      Look up a single element in an array
O(log n)        Logarithmic time   Find an item in a sorted array via binary search
O(n)            Linear time        Find an item in an unsorted array
O(n log n)      Log-linear time    Complex sorting such as heap sort and merge sort
O(n^2)          Quadratic time     Simple sorting such as bubble, selection, and insertion


O(1)- the operation does not depend on the size of the data set-- example: looking for
i[1] in an array.

O(log n)- as the number of items in an array grows, it only takes a logarithmic time
relationship to find any given item.

O(n)- linear time is the next step up from logarithmic time. As more items are added to an
array in an usorted fashion, it takes a corresponding linear time amount to perform a search
for an item.

The algorithm you choose will need to work well with the data structure into which your data
has been organized. Of course, the most common structures are:
arrays, linked lists, stacks, queues, trees, hash tables
