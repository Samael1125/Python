lst = [3,5,2,5,67,46,32,7,9,8]

print(lst)

# Access the Element through indexing
print(lst[0])
print(lst[4])
print(lst[-1])
print('-'*20)

# Modify values
print(lst)
lst[3]=10
print(lst)
print('-'*20)

# slicing
print(lst[1:4])
print('-'*20)

# reverse a list
print(lst[::-1])
print(reversed(lst))
print('-'*20)

print('-'*20)

print(lst[::-2])
print('-'*20)

# Appending 
lst.append(7)
print(lst)
print('-'*20)

# Removing 
lst.remove(5)
print(lst)
print('-'*20)

# Length
print(lst)
print(len(lst))
print('-'*20)

# Sorted
print(lst)
print(sorted(lst))
print('-'*20)

# finding min. & max.
print(lst)
print(min(lst))
print(max(lst))
print('-'*20)

# Iteration the elemnts of list | direct
print(lst)

for i in lst:
    print(i)

# Iteration the elemnts of list | Indexing
print(lst)

for i in range(len(lst)):
    print(lst[i])
 
# Iteration the elemnts of list in reverse
print(lst)

for i in range(len(lst)-1,-1,-1):
    print(lst[i])
 

print('-'*20)
print('-'*20)
print('-'*20)

# Multi-dimensional list

lst2 = [[1,2,3],[4,5,6],[7,8,9]]   # 2D list

print(lst2)


# Accessing the elements
print(lst2)
print(lst2[0][0])
print(lst2[2][1])
print(lst2[0])
print(lst2[2])
print('-'*20)

# Modify the values
print(lst2)
lst2[1][1]=9
print(lst2)
lst2[1]=['ashui',24]
print(lst2)
print('-'*20)

#appending the vlu
print(lst2)
lst.append([9,10,11])
print(lst2)
print('-'*20)

# delete the index
print(lst2)
del lst2[0]
print(lst)
print('-'*20)


lst2 = [[1,2,3],[4,5,6],[7,8,9]]
# length
print(lst2)
print(len(lst2))
print('-'*20)

# reverse
print(lst2)
print(lst2[::-1])
print('-'*20)

# Itreating all elements
print(lst2)
for i in lst2:
    for j in i:
        print(j)

print('-'*20)
print('-'*20)
print('-'*20)




# List comprehension
lst = [1,2,3,4,5,6]
print(lst)
lst = [i**2 for i in lst]
print(lst)
lst = [i**2 for i in lst]
print(lst)

# finding 1st 10 even no.
print([i for i in range(21) if i%2==0])
print('-'*20)

# finding 1st 10 even no. & sqr of it
print([i**2 for i in range(21) if i%2==0])
print('-'*20)

# Matrix
matrix = [[i * j for j in range(3)] for i in range(4)]
print(matrix)

# upprer case the letter
letters = ['a', 'b', 'c']
print([letter.upper() for letter in letters])





