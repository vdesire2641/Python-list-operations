# create a list with the following five items:
# 7, 9, 'a', 'cat', False.
# Assign this list to the variable myList
# 4.1
# 4.2
mylist = [7, 9, 'a', 'cat', False]
mylist.append(3.14)
mylist.append(7)
# printing the list after append operation
print(mylist)
mylist.insert(2, "dog")
# printing the list after insert operation
print(mylist)
# finding the position of the data
print(mylist.index('cat'))
# finding the occurrences of the data
print(mylist.count(7))
mylist.remove(7)
# doing the remove operation and then printing
print(mylist)
mylist.pop(mylist.index('dog'))
# printing the combination of two functions, pop and index which removes the data at the found index
print(mylist)

