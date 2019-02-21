text = '''title,author,year
The Weidstone of Brisingamen,Alan Garner,1960
Peridido Street Station,China Mieville,2000
Thudl,Terry Pratchett,2005
The Spellman Files,Lisa Luts,2007
Small Gods,Terry Pratchett,1992
'''
with open('books.csv', 'wt') as outfile:
    outfile.write(text)
