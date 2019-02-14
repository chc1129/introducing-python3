poem = ''
fin = open('relativity', 'rt')
#poem = fin.read()
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))
