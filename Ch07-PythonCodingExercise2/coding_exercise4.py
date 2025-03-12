def check_unique(lst):
    return len(set(lst)) == len(lst)

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 3, 4, 5]

print(check_unique(lst1))
print(check_unique(lst2))


