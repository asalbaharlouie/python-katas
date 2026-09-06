def split_even_odd(numbers):
    even_list = []
    odd_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    return even_list, odd_list 

print(split_even_odd([10, 32, 12, 87, 91, 10, 29, 54]))