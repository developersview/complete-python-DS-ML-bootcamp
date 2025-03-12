def is_subset(lst1, lst2):
    return all(x in lst2 for x in lst1)


def is_subset2(lst1, lst2):
    for item in lst1:
        if item not in lst2:
            return False
    return True


lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]

lst3 = [1, 6]
lst4 = [1, 2, 3, 4, 5]

print(is_subset(lst1, lst2))
print(is_subset2(lst1, lst2))

print(is_subset(lst3, lst4))
print(is_subset2(lst3, lst4))