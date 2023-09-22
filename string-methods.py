
#? String Methods 
    # syntax: string_name.string_method(arguments)

# Formatting Methods
    # .lower() - returns the string with all lowercase latters
    # .upper() - returns the string with all uppercase letters
    # .title() - returns the string with first letter of each work capitalized

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

# Splitting Strings 
    # .split() - splits a string into substrings based on the argument. If no argument is given it will split at spaces
    # puts the sub strings into a list 

line_one = "The sky has given over"

# splits the string on spaces
line_one_words = line_one.split()
print(line_one_words)

# splits the string based on the argument given (and the argument is removed from the string)
split_on_e = line_one.split('e')
print(split_on_e)

# splitting with escape sequences
    # \n newline - allows us to split multiline strings by line breaks
    # \t horizontal tab - allows us to split multiline strings by tabs

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)