import csv
with open('villains', 'rt') as fin: # コンテキストマネージャ
    #cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    cin = csv.DictReader(fin)
    villains = [row for row in cin] # リスト内包表記を使っている

print(villains)
