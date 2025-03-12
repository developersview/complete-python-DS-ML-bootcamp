def find_largest(numbers):
    if not numbers:
        return None
    
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers1 = [3, 8, 2, 10, 5]
print(find_largest(numbers1))

numbers2 = [-5, -10, -2, -1, -7]
print(find_largest(numbers2))