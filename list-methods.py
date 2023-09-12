
# ?Example syntax for methods
    # list.method(input)

# ?Example syntax for a built-in function 
    # builtinfunction(input)

#? Common Python List Methods
    # .count() - counts the number of times an element occurs in a list 
    # .insert() - insert an element into a specific index of a list 
    # .pop() - remove an element from a speicifc indec of a list OR from the end of a list
    # .sort() - sorts a list  

#? Common Python Built In Functions
    # range() - creates a sequence of integers 
    # len() - gets length of a list 
    # sorted() - sorts a list 
    

#! .insert()
    # takes 2 inputs: index you want to insert into, element you want to insert 
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
front_display_list.insert(0, 'Pineapple')
print(front_display_list)

#! .pop()
    # optional single input: index of the element you want to remove
    # if nothing is given, it will remove the last element 
    # will return the value removed when assigned to a variable 

removed_element = front_display_list.pop(1)
print(front_display_list)
print('Removed:', removed_element)

#! range()
    # takes single input and generates numbers starting at 0 and ending at the number before the input 
    # creates an object 
number_list = range(3)
print((number_list)) #prints an object 
print(list(number_list)) #need to change it to a list

    # can also take 2 inputs to signfiy starting/stopping point
number_list_2 = range(2,9)
print('number_list_2', list(number_list_2))

    # 3 inputs creates a list that starts, stops and skips by the 3rd input 
number_list_3 = range(2, 21, 2)
print('number_list_3', list(number_list_3))

#! len()
print('length',len(number_list_3))
length = len(number_list_3)
print(length)

big_range = range(2, 3000, 10)
big_range_length = len(big_range)
print('big_range_length',big_range_length)

#! slicing - divides a list 
    #syntax: list[start:end] prints the list that starts at index 'start' and ends one before index 'end'
    #syntax: list[:n] shows the first n elements of a list 
    #syntax: list[-n:] shows the last n elements of a list
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:4]
print(beginning)

beginning2 = suitcase[:3]
ending = suitcase[-3:]
print(beginning2)
print(ending)

#! .count()
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count('Jake')
print(jake_votes)

#! .sort() / sorted()
    #.sort() with no input will sort either alphebetically or numerically 

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities) #prints 'none' 
print(cities)

    #sorted() will generate a new list unlike .sort() which just sorts the original list 
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)
print(games)
print(games_sorted)

#practice 

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]
twin_beds = inventory.count('twin bed')
removed_item = inventory.pop(4)
inventory.insert(10,'19th Century Bed Frame')
inventory.sort()
print(inventory)

#? Tuples 
    # Tuples are like lists but it cannot be changed 

my_info = ('Amanda', 27, 'Developer')
print(my_info)
my_info[0]

# unpacking a tuple
name, age, occupation = my_info
print(name)
print(age)

#! zip()
    # zip() is a built in function that allows us to combine data sets 
    #i.e. make two dimensional lists 
    # inner lists don't use [], they use () and are tuples so they cannot be changed

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)
print(list(names_and_heights))

