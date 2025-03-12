def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))