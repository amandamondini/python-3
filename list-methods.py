
# ?Example syntax for methods
    # list.method(input)

# ?Example syntax for a built-in function 
    # builtinfunction(input)

#? Common Python List Methods
    # .count() - counts the number of times an element occurs in a list 
    # .insert() - insert an element into a specific index of a list 
    # .pop() - remove an element from a speicifc indec of a list OR from the end of a list
    # .sort() - sorts a list  

#? Common Python Built In FUnctions
    # range() - creates a sequence of integers 
    # len() - gets length of a list 
    # sorted() - sorts a list 
    

# .insert()
    # takes 2 inputs: index you want to insert into, element you want to insert 
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
front_display_list.insert(0, 'Pineapple')
print(front_display_list)

# .pop()
    # optional single input: index of the element you want to remove
    # if nothing is given, it will remove the last element 
    # will return the value removed when assigned to a variable 

removed_element = front_display_list.pop(1)
print(front_display_list)
print('Removed:', removed_element)

# range()
