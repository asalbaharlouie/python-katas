def merge_dicts(d1, d2):
    d3 = d1.copy() #با keys , values d1 شروع بشه

    for key in d2:
        d3[key] = d2[key] 
    
    return d3

print(merge_dicts({"a": 3, "b": 4, "c": 2}, {"a": 10, "d": 13}))