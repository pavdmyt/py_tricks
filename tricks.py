"""
My collection of Python tricks.
"""


#######################################################################
# Control flow

## 1
x = 2
result = 'greater' if x > 3 else 'less or equal'

# same as
y = 2
if y > 3:
    result = 'greater'
else:
    result = 'less or equal'

assert x == y, 'Control flow #1 failed!'

## 2
# `else` statements in `for`/`with` statements
# for val in values:
#     if val == 42:
#         break
# else:
#     print('No values contained 42!')


#######################################################################
# `zip`

## 1
lst = [('red', 210), ('green', 105), ('blue', 30)]
color, val = zip(*lst)

assert color == ('red', 'green', 'blue'), '`zip` #1 failed!'
assert val == (210, 105, 30),             '`zip` #1 failed!'

## 2
# matrix transpose
mtx = [(1, 2),
       (3, 4),
       (5, 6)]

assert zip(*mtx) == [(1, 3, 5), (2, 4, 6)], '`zip` #2 failed!'

## 3
# rotate a matrix by 90 degrees
assert zip(*mtx[::-1]) == [[5, 3, 1], [6, 4, 2]], '`zip` #3 failed!'

## 4
# clustering a data series into n-length groups
seq = range(1, 10)
assert zip(*[iter(seq)]*3) == [(1, 2, 3), (4, 5, 6), (7, 8, 9)], '`zip` #4 failed!'

# explanation:
x = iter(range(1, 10))
assert zip(x, x, x) == zip(*[iter(seq)]*3), '`zip` #4 failed!'


## 5
# invert a dictionary using `zip`
d = dict(red=210, green=105, blue=30)

inv_d1 = dict(zip(d.values(), d.keys()))  # `zip`
inv_d2 = dict(map(reversed, d.items()))   # `map`
inv_d3 = {v: k for k, v in d.items()}     # dict comprehension (python >= 2.7)

assert inv_d1 == inv_d2 == inv_d3, '`zip` #5 failed!'

##### Flattening lists
lst = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]

flat1 = sum(lst, [])
flat2 = [item for sublist in l for item in sublist]  # fastest way

assert flat1 == flat2, 'List flattening failed!'


##### Unordered stuff

## `start` parameter in `enumerate`
dct = {'four': 4, 'five': 5, 'six': 6}

# lst = ['four', 'five', 'six']
for ind, val in enumerate(dct.values(), start=4):
    assert ind == dct[val], '`enumerate` failed!'

## unpacking sequences (works in Python 3)
# works with tuples, sets and strings

seq = range(1, 6)
a, b, *c = seq  # a=1, b=2, c=[3,4,5]
a, *b, c = seq  # a=1, b=[2,3,4], c=5

assert a == 1 and b == [2, 3, 4] and c == 5, 'Sequences unpacking failed!'
