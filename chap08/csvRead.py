import csv
with open('villains', 'rt') as fin: # コンテキストマネージャ
    cin = csv.reader(fin)
    villains = [row for row in cin] # リスト内包表記を使っている

print(villains)
