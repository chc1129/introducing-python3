# 60 sec/min * 60 min/hr * 24 hr/day
seconds_per_day = 86400
seconds_per_day = 86400 # 60 sec/min 60 min/hr * 24 hr/day
# I can say anything here, even if Python doesn't like it,
# because I'm protected by the awesome
# octothorpe.
print("No comment: quotes make the # harmless.")
alphabet = ''
print(alphabet)
alphabet += 'abcdefg'
print(alphabet)
alphabet += 'hijklmnop'
print(alphabet)
alphabet += 'qrstuv'
print(alphabet)
alphabet += 'wxyz'
print(alphabet)

alphabet = 'abcdefg' + \
    'hijklmnop' + \
    'qrstuv' + \
    'wxyz'
print(alphabet)
print(1 + 2 + \
        3)

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!.")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

x = 7
print(x == 5)
print(x == 7)
print(5 < x)
print(x < 10)
print(5 < x and x < 10)
print((5 < x) and (x < 10))
print(5 < x or x < 10)
print(5 < x and x > 10)
print(5 < x and not x > 10)
print(5 < x < 10)
print(5 < x < 10 < 999)

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

count = 1
while count <= 5:
    print(count)
    count += 1

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even nmber', number)
        break
    position += 1
else:   # breakが呼び出されない
    print('No even number found')

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Pater']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1
print()

for rabbit in rabbits:
    print(rabbit)
print()

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation: # または for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'bas the contents', contents)

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:   # breakしていないということはチーズがないということ
    print('This is not much of a cheese shop, is it?')

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'puddingi']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list( zip(english, french) ))
print(dict( zip(english, french) ))

for x in range(0, 3):
    print(x)

print(list( range(0, 3) ))

for x in range(2, -1, -1):
    print(x)

print(list( range(2, -1, -1) ))

print(list( range(0, 11, 2) ))
