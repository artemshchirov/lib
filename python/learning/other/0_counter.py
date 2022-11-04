from collections import Counter

number_list = [1, 1, 1, 77, 4, 5, 4, 77, 'hi', 'wow', 'hi', 'hi']
print(Counter(number_list))

string = 'dddddddkkkkkkkkiiiiiiiii'
print(Counter(string))

sentence = "Hello how are you doing? Hello I`m fine. How do you do? Hey hey hey"
c = Counter(sentence.split(' '))
print(sum(c.values()))
print(list(c))
print(set(c))
print(dict(c))
s = c.items()
print(s)
s = Counter(dict(s))
print(s)
print(c.most_common(3)[:-3:-1])
c.clear()
print(sum(c.values()))
