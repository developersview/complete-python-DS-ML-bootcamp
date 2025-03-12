def is_palindromic_tuple(tup):
    return tup[::1] == tup[::-1]

tpl1 = (1, 2, 3, 2, 1)
tpl2 = ('a', 'b', 'c', 'b', 'a')
tpl3 = (1, 2, 3, 4, 5)
tpl4 = ('x', 'y', 'z', 'x')
tpl5 = ('a',)

print(is_palindromic_tuple(tpl1))
print(is_palindromic_tuple(tpl2))
print(is_palindromic_tuple(tpl3))
print(is_palindromic_tuple(tpl4))
print(is_palindromic_tuple(tpl5))



