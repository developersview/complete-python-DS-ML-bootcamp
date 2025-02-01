def rotate_list(lst, k):
    if not lst:
        return []
    k = k % len(lst)
    return  lst [len(lst) - k:] + lst[:-k]

lst1 = [1, 2, 3, 4, 5]
k1 = 2

lst2 = [10, 20, 30, 40, 50]
k2 = 3

print(rotate_list(lst1, k1))
print(rotate_list(lst2, k2))