# sets is a collection of unique element
# unique elememt --> element that cannot be repeated
# ex. {1,2} ans in this we cannot add 1 or 2

myset = set()
myset.add(5)
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.add(5)  # hte set will print bt only with unique value
print(myset)

set1 = {1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 4, 5, 4, 5, 6, 3, 4}
set(set1)
print(set1)  # here all the repeated element get ignored and only printed once


print(set("parellel"))

print(set('mississippi'))
