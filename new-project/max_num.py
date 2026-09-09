def find_max(MyList):
    max_num = MyList[0]
    for i in MyList:
        if i > max_num:
            max_num = i
    return max_num


print(find_max([-3, -29, -0.5, -4]))
