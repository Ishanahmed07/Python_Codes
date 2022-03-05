# Tuples are immutable that means they cannot be change
# For creating a tuple we use parenthesis


t = (1, 2, 3)
# print(type(t))
# print(t)
# we can use indexing also for grabbing the element in the tuple


# two built in function of tuples are

t1 = ('a', 'a', 'b')
# count function will give the count of an objevct that have been appear in the tuple
print(t1.count('a'))


# the other one is index function that return the very first index of the given object
print(t1.index('b'))


# if we are assigning a value to the index in list that can be possible bt in tuple it gives u err
# ex.  mylist[0]='new' --> will execute
#  t1[0]='new' --> error
