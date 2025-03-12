def count_even_odd(lst):
    even_count = 0
    odd_count = 0

    for item in lst:
        if item % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return (even_count, odd_count)

lst = [1, 2, 3, 4, 5]

print(count_even_odd(lst))