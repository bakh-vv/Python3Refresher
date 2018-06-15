print("I'm Python. Nice to meet you!")

"{} can be {}".format("Strings", "interpolated")

"yahoo!" if 3 > 2 else 2 

li = []
li.append(1)
li.append(2) 

li[::2]
li[::-1]

# Insert an element at a specific index
li.insert(1, 2)

other_li = [4, 5, 6]
li.extend(other_li)

# Check for existence in a list with "in"
1 in li # => True

len(li)  # => 6

# Tuples are like lists but are immutable.
tup = (1, 2, 3)

# unpack tuples (or lists) into variables
a, b, c = (1, 2, 3) 
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4) # b is now [2, 3]
d, e, f = 4, 5, 6
# swap two values
e, d = d, e  

# Dictionaries 
filled_dict = {"one": 1, "two": 2, "three": 3}

# keys for dictionaries have to be immutable types. Immutable types include ints, floats, strings, tuples.
valid_dict = {(1,2,3):[1,2,3]}

# Check for existence of keys (NOT values) in a dictionary with "in"
"one" in filled_dict

# Use "get()" method to avoid the KeyError
filled_dict.get("four")

# The get method supports a default argument when the value is missing
filled_dict.get("four", 4)

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)

# Adding to a dictionary
filled_dict.update({"four":4})
filled_dict["four"] = 4

del filled_dict["one"]

empty_set = set()
some_set = {1, 1, 2, 2, 3, 4}

filled_set = some_set
filled_set.add(5)

# set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}
# set union with |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}
# set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}
# set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
# set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False
# set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3} # => True

# Check for existence in a set with in
2 in filled_set   # => True

# Indentation is significant in Python!
# Convention is to use four spaces, not tabs.
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")

"""
For loops iterate over lists

"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""

While loops go until a condition is no longer met.

"""
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1

# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")

with open("myfile.txt") as f:
    for line in f:
        print(line)

# The Iterable.
# An iterable is an object that can be treated as a sequence.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.

# We can loop over it.
for i in our_iterable:
    print(i)  # Prints one, two, three

# cannot address elements by index.
our_iterable[1]  # Raises a TypeError

# can create an iterator.
our_iterator = iter(our_iterable)
# Our iterator is an object that can remember the state as we traverse through it.
next(our_iterator)  # => "one"
# It maintains state as we iterate.
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"
next(our_iterator)  # Raises StopIteration

# You can grab all the elements of an iterator by calling list() on it.
list(filled_dict.keys())
