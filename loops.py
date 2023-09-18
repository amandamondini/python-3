
#? For Loops
    # syntax: for <temp variable> in <collection/list>: action
    # indentation: everything at the same level of indentation after the for loop decleration is included in the loop body 
    
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

for game in board_games:
    print(game)


# using for loops and range will do the action for the length of the range
promise = "I will finish the python loops module!"

for i in range(5):
    print(promise)


#? While Loops
    # syntax: while <conditional statement>: actioncountdown = 10

countdown = 10
while countdown>=0:
    print(countdown)
    countdown += -1

# while loop example with lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
    print('I am learning about', python_topics[index])
    index+= 1

#! Loop Controls (break, continue)

#? Break 
    #break will break out of the loop once a condition is met 

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print('They have the dog I want!')
        break

#? Continue 
    # loop will continue based on a condition
    # will move onto the next element if condition isn't true 
    
# example: only print ages >=21    
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for i in ages:
    if i < 21:
        continue
    print(i)
    

#? Nested Loops
# nested loops allow you to loop through lists that have lists 
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

#loops through each sublist
for location in sales_data:
    print(location)
    #loop elements in each sublist
    for scoops in location:
        scoops_sold += scoops

print(scoops_sold)