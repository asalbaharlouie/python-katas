def reverse_string(word):
    reverse_str = "" #رشته جدید این تو ریخته میشه
    for char in word:
        reverse_str = char + reverse_str  #هر حرف جدید میره اول صف، پس کلمه عکس میشه

    return reverse_str

print(reverse_string("salam"))