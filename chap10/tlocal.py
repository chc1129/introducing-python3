import locale
from datetime import date

halloween = date(2014, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is', 'ja_JP', 'zh_TW']:
    print(locale.setlocale(locale.LC_TIME, lang_country))
    print(halloween.strftime('%A, %B %d'))

names = locale.locale_alias.keys()
good_names = [name for name in names if \
    len(name) == 5 and name[2] == '_']

print(good_names[:5])
de = [name for name in good_names if name.startswith('de')]
print(de)

ja = [name for name in names if name.startswith('ja')]
print(ja)

