
#? Lists 
    # built in data structure that allows us to work with a collection of data in a a sequential order
    # syntax: [a, b, c, d] 
    # can contain multiple data types, including other lists 

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

    #using index to print one value in a list 
print(list2[1])

    # using index -1 selects that last element of a list (-2 gets the second to last and so on)
print(list_combined[-1])

    #to replace an element into a specific spot 
list2[1] = 'peach'
print(list2)

    # removing items from a list 
list2.remove('peach')
print(list2)

#? Example

gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

#adding grades to gradebook
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])

#changing the value of a grade at position -1, 1
gradebook[-1][1] = 98

#removing and adding values for poetry class
gradebook[2].remove(85)
gradebook[2].append('Pass')

print(gradebook)

#adding two lists 
last_semester_gradebook = [['math', 90], ['science', 89]]
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)


