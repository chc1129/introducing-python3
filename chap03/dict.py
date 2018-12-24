empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
    }
print(bierce)

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))

tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
print(dict(tol))

los = ['ab', 'cd', 'ef']
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
print(pythons)

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
    'Graham': 'Chapmain',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
    }
print(some_pythons)

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Falin': 'Micheal'
    }
print(pythons)

others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
print(others)

pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)

del pythons['Marx']
print(pythons)

del pythons['Howard']
print(pythons)

pythons.clear()
print(pythons)

pythons = {}
print(pythons)

pythons = {'Chapman': 'Graham', 'Cleese': 'John',
    'Jones': 'Terry', 'Falin': 'Michael'}
print(pythons)
print('Chapman' in pythons)
print('Falin' in pythons)
print('Gillian' in pythons)
print(pythons['Cleese'])
#print(pythons['Marx']) # exception
print('Marx' in pythons)
print(pythons.get('Gleese'))
print(pythons.get('Marx', 'Not a Python'))

signals = {'green': 'go', 'yellow': 'go faster',
    'red': 'smile for the camera'}
print(signals.keys())

print(list( signals.values() ))

