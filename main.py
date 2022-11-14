dic = {}
original = input()
cipher = input()

for i in range(len(cipher)):
    key = cipher[i]
    val = original[i]
    if key not in dic:
        dic[key] = val

decoded = ''
encoded = input()
for c in encoded:
    if c in dic:
        decoded += dic[c]
    else:
        decoded += '.'

print(decoded)