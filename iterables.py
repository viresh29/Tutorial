import os
import glob
from pprint import pprint as pp
file_size = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob('*.py')}

pp(file_size)



words = "why sometimes I have believed as many as six impossible things before breakfast".split()

print(words)

print([len(word) for word in words])

# [expr(item) for item in iterable]


iterables = ['Spring','Summer','Autumn','Winter']

iterator = iter(iterables)

print(next(iterator))


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

print(first(["1st","2nd","3rd"]))
