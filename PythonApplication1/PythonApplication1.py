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

