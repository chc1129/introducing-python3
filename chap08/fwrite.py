test1 = 'This is a test of the mergency text system'
print(len(test1))

outfile = open('test.txt', 'wt')
outfile.write(test1)
outfile.close()

with open('test.txt', 'rt') as infile:
    test2 = infile.read()

print(len(test2))
print(test1 == test2)
