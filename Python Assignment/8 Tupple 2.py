# tuple

# tuple : tuple is a collection data type which is represent by (), tuple is orderable, indexable, and immutable

# difference between list and tuple

# list : list is collection data type which is mutable (we can change it value)

# tuple : tuple is a collection data type but which is immutable (we can't change it value)

t = ()

print(t)
print(type(t))

t = ("python")
print(type(t))

t = (12,23,45,67,89,12)

list_1 = list(t)

list_1.remove(12)
t = tuple(list_1)
print(12)
print(t)