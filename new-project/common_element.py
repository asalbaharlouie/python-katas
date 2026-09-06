def common_elements(list1, list2):
    my_set1 = set(list1) 
    my_set2 = set(list2)
    res = set()
#داره رو تک تک آیتم های my_set1 راه میره 
    for item in my_set1:
#پی اینجا آیتم های my_set2 رو باهاش مقایسه میکنیم
        if item in my_set2: 
            res.add(item)
    return res

print(common_elements([1, 9, 21, 11], [11, 21, 1, 1, 8, 3]))