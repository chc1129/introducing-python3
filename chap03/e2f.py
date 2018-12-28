e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)
print(e2f["walrus"])
f2e = {value: key for key, value in e2f.items()}
print(f2e)
print(f2e["chien"])
print(set(e2f))
