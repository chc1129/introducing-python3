empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednewsday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
another_empty_list = list()
print(another_empty_list)
print()

print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

birthday = '1/6/1952'
print(list(birthday))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('//'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
marxes[2] = 'Wanda'
print(marxes)
print()

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])
print()

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)
print()

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Earl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Earl']
marxes += others
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Earl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')
print(marxes)
marxes.insert(10, 'Karl')
print(marxes)

del marxes[-1]
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print(marxes[2])

del marxes[2]
print(marxes)

print(marxes[2])
print()

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
marxes.pop(1)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))
print()

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Groucho' in marxes
'Bob' in marxes
print()

words = ['a', 'deer', 'a', 'female', 'deer']
print('deer' is words)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

marxes = ['Groucho', 'Chino', 'Harpo']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)

print()

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)

marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))

print()

a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'surprise'
print(a)
print(b)
b[0] = 'I hate surpreises'
print(b)
print(a)

a = [1, 2, 3]
print(a)
b = a.copy()
print(b)
c = list(a)
print(c)
d = a[:]
print(d)

a[0] = 'interger lists are boring'
print(a)
print(b)
print(c)
print(d)
