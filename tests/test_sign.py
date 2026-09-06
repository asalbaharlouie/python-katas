def sign(num):
    if num >= 1:
        return 1
    elif num <= -1:
        return -1
    else:
        return 0

def test_sign_positive_number():
    assert sign(12) == 1 

test_sign_positive_number()

def test_sign_negative_number():
    assert sign(-10) == -1

test_sign_negative_number()

def test_sign_zero():
    assert sign(0) == 0

test_sign_zero()

print(sign(-8))
print(sign(6))
print(sign(0))