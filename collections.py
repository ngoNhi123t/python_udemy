from collections import Counter
# Counter with list

lst = [1,1,1,1,4,11,2,3,4,2,3,42,2,2,3,3,4,4]
print(Counter(lst))

#Counter with string

print(Counter('nhdfbhsjnfksjghksa'))

#Counter with word in sentences
s = ' how many are there how'
words = s.split()
print(Counter(words))
c = Counter(words)
print(c.most_common(2))

lt = [1,1,1,2,2,2,3,3]
d = Counter(lt)
# total of all counts( có bao nhiêu phần tử)
print(sum(d.values()))


# reset all counts
# print(d.clear())


#list unique elements
print(list(d))


# convert to a set 
print(set(d))


# convet to a regular dictionary
print(dict(d))

#convert to a list of (elem, cnt) pairs
print(d.items())


# n least common elements
# d.most_common()[:-n-1:-1] 


  # remove zero and negative counts
d += Counter()                



# DEFAULTDICT

# keyerror
from collections import defaultdict
d ={}
# print(d['one'])
d = defaultdict(object)
d['one']
for item in d:
    print(item)
d=defaultdict(lambda: 0)
print(d['one'])

#Nametuple

from collections import namedtuple
Dog = namedtuple('Dog', ['age','breed','name'])
sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")
print(sam)
print(sam.age)