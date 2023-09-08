
#? Lists 
    # built in data structure that allows us to work with a collection of data in a a sequential order
    # syntax: [a, b, c, d] 
    # can contain multiple data types 

my_list = ['Sam', 67, 85.5, True]
print(my_list)

#? Lists & Methods 
    # syntax: listname.methodname()
my_list.append(5) #adds the number 5 to the end of the list 
my_list.append('word')
print(my_list)

    # use + to add multiple items from one list to another 
list2 = ['apple', 'pear']
list3 = ['banana']
list_combined = list2 + list3
print(list_combined)
