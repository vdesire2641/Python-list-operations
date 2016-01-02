# although python provides us with many list methods
# it is good practice and very instructive to think
# about how they implemented. implement a python function
# that works like the following
# count, in- return true of item in the list
# reverse, index- return -1 if not in the list
# insert
def initialist(n):
    numbers = n
    numbers.count(4)
    print(numbers.count(4))
    if 10 in numbers:
        print('true')
    if numbers.index(2) not in numbers:
        print('-1')
        numbers.insert(3, 'ishna')
    print(numbers)
    numbers.reverse()
    newlist = numbers
    print(newlist)
initialist([2, 4, 6, 8, 10, 8, 7, 6, 5, 4, 3, 2])








