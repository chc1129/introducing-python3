snowman = 'u\2603'
print(len(snowman))
ds = snowman.encode('utf-8')
print(len(ds))
print(ds)
print(snowman.encode('ascii', 'ignore'))
print(snowman.encode('ascii', 'replace'))
print(snowman.encode('ascii', 'backslashreplace'))
print(snowman.encode('ascii', 'xmlcharrefreplace'))
