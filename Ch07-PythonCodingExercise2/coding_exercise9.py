def merge_two_sorted_lists(list1, list2):
    return sorted(list1 + list2)

list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(merge_two_sorted_lists(list1, list2))