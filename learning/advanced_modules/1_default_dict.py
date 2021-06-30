from collections import defaultdict


my_dict1 = defaultdict(object)
my_dict1[1] = 'a'
print(my_dict1[2])

my_dict2 = defaultdict(list)
print(my_dict2[2])

my_dict3 = defaultdict(set)
print(my_dict3[2])

my_dict4 = defaultdict(lambda: 1)
print(my_dict4[2])

s = "Hello"
d = defaultdict(int)
for k in s:
    d[k] += 1
print(sorted(d.items()))
