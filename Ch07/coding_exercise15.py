from collections import defaultdict
from collections import Counter

def merge_dicts_with_overlapping_keys1(dicts):
    merged_dict = defaultdict(int)  # Default value for missing keys is 0
    
    for d in dicts:
        for key, value in d.items():
            merged_dict[key] += value  # Sum values for overlapping keys
    
    return dict(merged_dict)  # Convert defaultdict to a regular dictionary


def merge_dicts_with_overlapping_keys2(dicts):
    merged_dict = Counter()  # Uses Counter to sum values
    for d in dicts:
        merged_dict.update(d)  # Adds values for matching keys
    return dict(merged_dict)


def merge_dicts_with_overlapping_keys3(dicts):
    # Initialize an empty dictionary to store the result
    result = {}
    
    # Loop through each dictionary in the list
    for d in dicts:
        # Loop through each key-value pair in the current dictionary
        for key, value in d.items():
            # If the key is already in the result dictionary, add the new value to the existing value
            if key in result:
                result[key] += value
            # Otherwise, add the key-value pair to the result dictionary
            else:
                result[key] = value
    
    return result


# Example usage
print(merge_dicts_with_overlapping_keys1([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]))
print(merge_dicts_with_overlapping_keys1([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))

# Example usage
print(merge_dicts_with_overlapping_keys2([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]))
print(merge_dicts_with_overlapping_keys2([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))

# Example usage
print(merge_dicts_with_overlapping_keys3([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]))
print(merge_dicts_with_overlapping_keys3([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))

