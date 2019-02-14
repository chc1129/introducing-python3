bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
#fout.write(bdata)
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fout.close()
