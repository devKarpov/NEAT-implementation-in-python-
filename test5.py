
import random

a = [0,1]
b = [0,1,4,9,16,25,36,49,64,81]

frac = 0.8  # how much of a/b do you want to exclude

# generate a list of indices to exclude. Turn in into a set for O(1) lookup time
inds = set(random.sample(list(range(len(a))), int(frac*len(a))))

# use `enumerate` to get list indices as well as elements. 
# Filter by index, but take only the elements
new_a = [n for i,n in enumerate(a) if i not in inds]
new_b = [n for i,n in enumerate(b) if i not in inds]

#print(random.random())
while True:
    r = random.random()
    if r < 0.001:
        print(r)