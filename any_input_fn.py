def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
        return sum
    
print(add(1, 2, 3, 4))
