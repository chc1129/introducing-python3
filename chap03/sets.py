empty_set = set()
print(empty_set)
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)
print(set( 'letters' ))
print(set( ['Dasber', 'Dancer', 'Prancer', 'Mason-Dixon'] ))
print(set( ('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} ))

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
    }

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
        'cream' in contents):
        print(name)

for name, contents in drinks.items():
    if  contents & {'verouth' 'orange juice'}:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']
print(bruss)
print(wruss)

a = {1, 2}
b = {2, 3}

print (a & b)
print(a.intersection(b))
print(bruss & wruss)

print(a | b)
print(a.union(b))
print(bruss | wruss)

print(a - b)
print(a.difference(b))

print(bruss - wruss)
print(wruss - bruss)

print(a ^ b)
print(a.symmetric_difference(b))

print(bruss ^ wruss)

print(a <= b)
print(a.issubset(b))

print(bruss <= wruss)

print(a <= a)
print(a.issubset(a))

print(a < b)
print(a < a)

print(bruss < wruss)

print(a >= b)
print(a.issuperset(b))

print(wruss >= bruss)

print(a >= a)
print(a.issuperset(a))

print(a > b)

print(wruss > bruss)

print(a > a)

print()

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
print(marx_list[2])
print(marx_dict['Harpo'])

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Meo', 'Curly', 'Larry']
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

houses = {
    (44.79, -93,14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House'
    }
print(houses)
