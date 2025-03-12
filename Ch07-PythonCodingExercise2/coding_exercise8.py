def max_consecutive_difference(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) < 2:
        return None
    return max(abs(b - a) for a, b in zip(lst, lst[1:]))


lst1 = [1, 7, 3, 10, 5]
lst2 = [10, 11, 15, 3]
lst3 = [1]
lst4 = []


print(max_consecutive_difference(lst1))
print(max_consecutive_difference(lst2))
print(max_consecutive_difference(lst3))
print(max_consecutive_difference(lst4))