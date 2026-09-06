def sign(num):
    if num >= 1:
        return 1
    elif num <= -1:
        return -1
    else:
        return 0

print(sign(-8))
print(sign(6))
print(sign(0))