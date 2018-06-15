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





