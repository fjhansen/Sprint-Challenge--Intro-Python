import pprint
pp = pprint.PrettyPrinter(indent=4)

# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

pp.pprint(humans)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [i.name for i in humans if i.name[0] == 'D']
pp.pprint(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [i.name for i in humans if i.name.endswith('e')]
pp.pprint(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [i.name for i in humans if 'C' <= i.name[0] <= 'G'] 
pp.pprint(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i.age + 10 for i in humans]
pp.pprint(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [i.name + '-' + str(i.age) for i in humans]
pp.pprint(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
##f = [(n.name, a.age) for n in humans for a in humans if 27 <= a.age <= 32]
f = [(i.name, i.age) for i in humans if 27 <= i.age <= 32]
pp.pprint(f)


# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(i.name.upper(), i.age+5) for i in humans]
pp.pprint(g)


# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(i.age) for i in humans]
pp.pprint(h)
