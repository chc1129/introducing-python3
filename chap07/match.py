import re
source = 'Young Frankenstein'
m = re.match('You', source) # matchはsourceの先頭がパターンに一致するかどうかを見る
if m:   # matchはオブジェクトを返す。マッチした部分を確かめる
    print(m.group())

m = re.match('^You', source) # パターンの先頭に^を付けても同じ意味になる
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.search(',*Frank', source)
if m:   # matchはオブジェクトを返す
    print(m.group())
