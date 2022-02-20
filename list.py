# list are ordered sequence that store the variety of data
#   [] with commas is used for separating
# Ex. [1,5,6,8,4]

# my_list = ['hello', 6, 'sohail']
# print(len(my_list))
# print(my_list[1:])

# another_list = ['yusuf', 8, 6, 'm']
# print(my_list+another_list)


l1 = ['one', 'two', 'three']
l2 = ['four', 'five']
# print(l1+l2)
l3 = l1+l2
print(l3)

l1[0] = 'zero'
# print(l1)
l3.append('six')  # append keyword is used to add element in the list at the end
l3.append('seven')


print(l3)
poped_elemtent = l3.pop()  # pop keyword is used to remove the elemeent top most element
print(poped_elemtent)
print(l3)


l4 = ['a', 'b', 'e', 't']
l4.sort()  # sort the list in the order
print(l4)

print(l4[1:])


l4.reverse()
print(l4)
