number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

number_list = list(range(1, 6))
print(number_list)

number_list = [number for nuber in range(1, 6)]
print(number_list)

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)

a_list = []
for nubmer in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)

rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

number_thing = (number for number in range(1, 6))
print(type(number_thing))
for number in number_thing:
    print(number)

number_thing = (number for number in range(1, 6))
number_list = list(number_thing)
print(number_list)

try_again = list(number_thing)
print(try_again)
