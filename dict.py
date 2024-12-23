dct = {1 : 1, 2 : 8, 3 : 27, 4 : 64, 5 : 125}
print(dct)

print(dct[1])
print(dct[4])
print('-'*50)

# Adding and updating the key-vlue
print(dct)
dct[6]=256
del dct[6]
print(dct)
print('-'*50)

#clearing the dict.
print(dct)
dct.clear()
print(dct)

# Iterating through the dict.
dct = {1 : 1, 2 : 8, 3 : 27, 4 : 64, 5 : 125}
print(dct)
print(dct.keys())
print(dct.values())
print('-'*50)

for k in dct.keys():
    print(k,dct[k])
print('-'*50)

print(dct.items())
for i in dct.items():
    # print(i)
    print(i[0],i[1])

        # or 
print('-'*50)
for k,v in dct.items():
    print(k,v)
print('-'*50)

# Check if key is present or not
print(dct)
print(1 in dct)
print('1' in dct)

# dict Merging the dict
dct1 = {1 : 'A', 2 : 'B', 3 : 'C'}
dct2 = {4 : 'D', 5 : 'E', 6 : 'F'}

dct1.update(dct2)
print(dct1)
print(dct2)



