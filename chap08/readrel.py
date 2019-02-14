poem = ''
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
#poem = fin.read()
#chunk = 100
#while True:
#    fragment = fin.read(chunk)
#    line = fin.readline()
#    if not fragment:
#    if not line:
#        break
#    poem += fragment
#    poem += line
print(len(lines), 'lines read')
#for line in fin:
#        poem += line
for line in lines:
    print(line, end='')

#fin.close()
#print(len(poem))
