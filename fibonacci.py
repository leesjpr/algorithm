
"""
    Num: 10
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""

def fibonacci(num):
    a, b = 0, 1
    result = []
    for item in range(num + 1):
        result.append(a)
        a, b = b, a + b

    return result[num]

print(fibonacci(10))

