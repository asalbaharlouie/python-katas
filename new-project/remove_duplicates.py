def remove_duplicates(items):
    seen_list = []
    seen_set = set()
    for item in items:
        if item not in seen_set:
            seen_list.append(item)
            seen_set.add(item)

    return seen_list 

print(remove_duplicates([1, 2, 4, 4, 3, 1, 2, 2]))