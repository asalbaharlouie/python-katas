def is_palindrome(word):
    reverse_str = ""
    for char in word:
        reverse_str = char + reverse_str
    if word == reverse_str:
        return True
    else: 
        return False 
    #اینجا همچین چیزی هم میتونیم بنویسیم return word == reverse_str

print(is_palindrome("bahar"))