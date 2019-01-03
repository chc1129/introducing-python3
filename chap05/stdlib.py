periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)

helium = periodic_table.setdefault('Helium', 947)
print(helium)

print(periodic_table)
