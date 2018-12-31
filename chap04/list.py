for x in [3, 2, 1, 0]:
    print(x)

y = [number for number in range(10) if number % 2 == 0]
print(y)

squares = {x: x*x for x in range(10)}
print(squares)

odd = {number for number in range(10) if number % 2 == 1}
print(odd)

for num in ('Got %s' % number for number in range(10)):
    print(num)

