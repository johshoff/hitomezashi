#!/usr/bin/env python3
# Hitomezashi stitch pattern
# inspired by https://www.youtube.com/watch?v=JbfhzlMk2eY
import random

width = 40
height = 40
dim = (width+height)//2

def biased(i):
    # random in the middle and biased toward the sides
    # the higher the factor, the more pronounced the bias is
    factor = 1.5
    return ((i/dim)-0.5)*factor+0.5

u = [bool(random.random() > biased(i)) for i in range(dim)]
v = [bool(random.random() > biased(i)) for i in range(dim)]

# completely random:
#u = [bool(random.getrandbits(1)) for i in range(dim)]
#v = [bool(random.getrandbits(1)) for i in range(dim)]

print()
for y in range(height):
    line = ' '
    for x in range(width):
        if (x+y) % 2 == 0:
            start = u[(x+y)//2]
            line += '/' if (start == (x%2 == 0)) else ' '
        else:
            start = v[(height+x-y)//2]
            line += '\\' if (start == (y%2 == 0)) else ' '
    print(line)
print()
