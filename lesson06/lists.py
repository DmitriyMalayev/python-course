users = ["John", "Sara", "Dave"]

data = ["Dave", 42, True]

emptylist = []

# print("Dave" in emptylist)

# print(users[0])
# print(users[-2])

# print(users.index('Sara'))

# print(users[0:2])
# print(users[1:])
# print(users[-3:-1])

# print(len(data))

# users.append('Elsa')
# print(users)

# users += ['Jason']
# print(users)


# users.extend(['Robert', 'Jimmy'])
# print(users)

# # users.extend(data)
# # print(users)

# users.insert(0, 'Bob') #Added to beginning of the list
# print(users)

# users[2:2] = ['Eddie', 'Alex'] #Added not replaced anyone
# print(users)

# users[1:3] = ['Robert', 'JPJ']  #replaced two values
# print(users)

# users.remove('Bob')  #first user
# print(users)

# print(users.pop()) #last user. Returns user removed.
# print(users)

# del users[0]  #specify index
# print(users)

# # del data
# print(data)  #error

# data.clear() #empties list but list exists
# print(data)
print(users)

users[1:2] = ["dave"]
print(users)
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 40, 42, 78, 1, 5, 100]
nums.sort()
print(nums)

nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))  # doesn't mutate
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(("Dave", 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
anotherTuple = list()
anotherTuple.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))  # returns number of occurences


# Lists and Tuples
# Lists use [] and are mutable
# Tuples use () and are immutable
# They both are ordered, have indexing / slicing methods, and duplicate elements
# Sets
# Sets are not ordered, not index based, don't have duplicate elements
