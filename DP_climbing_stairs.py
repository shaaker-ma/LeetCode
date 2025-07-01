def func(num):
    """
    Calculate the number of distinct ways to climb a staircase with `num` steps,
    where you can take either 1 or 2 steps at a time.
    """
    if num <= 2:
        return num
    a, b = 1, 2  # ways to reach step 1 and 2
    for i in range(3, num + 1):
        a, b = b, a + b
    return b
