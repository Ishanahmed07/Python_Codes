# dictionary is used to store the key for the data which can be easuly retrive by the user
dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dict)
print(dict['key1'])

# in the  list we can add list also and another dictionary also

prices = {'Apples': 50}
print(prices['Apples'])


myDict = {'key1': [2, 32, 5, 3, 7, 5]}
print(myDict['key1'][1])

# adding the new element to the dictionary
dict['key4'] = 'value4'
print(dict)


dict['key1'] = 'new value'
print(dict)

# want to see the see the keys of a dictonairy \
print(dict.keys())

# want to see the values of dictionary
print(dict.values())

# if we want to see the items of the dictionary
print(dict.items())
