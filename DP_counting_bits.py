def func(n):
    """
    0: 0000 0
    1: 0001 1
    2: 0010 1
    3: 0011 2
    4: 0100 1
    5: 0101 2
    6: 0110 2
    7: 0111 3
    8: 1000 1
    """
    bits = [0]* (n+1)
    for i in range(1, n+1):
        if(i%2 == 0):
            bits[i] = bits[i//2]
        else:
            bits[i] = bits[i//2] + 1
    return bits
    
n = 2
print(func(n))
n = 5
print(func(n))
n = 8
print(func(n))