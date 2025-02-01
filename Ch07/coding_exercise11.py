def merge_lists_to_dictionary(keys, values):
    if(len(keys) != len(values)):
        return False
    merged_dict = dict(zip(keys, values))
    return merged_dict



keys = ['a', 'b', 'c']; values = [1, 2, 3]

print(merge_lists_to_dictionary(keys, values))