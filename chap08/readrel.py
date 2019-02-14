poem = ''
fin = open('relativity', 'rt')
#poem = fin.read()
#chunk = 100
while True:
#    fragment = fin.read(chunk)
    line = fin.readline()
#    if not fragment:
    if not line:
        break
#    poem += fragment
    poem += line

for line in fin:
        poem = linsj

fin.close()
print(len(poem))
