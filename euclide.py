"""
    LCM: Least Common Multiple
        LCM = (A*B)/GCD
    GCD: Greatest Common Denominator
        GCD = (A*B)/LCM
    
"""

def gcdlcm(a, b):
    lcm = 0
    gcd = 0
    index = 1 

    large = a
    small = b
    if a < b:
        large = b
        small = a

    while(small):
        tmp = large * index

        if tmp%small == 0:
            gcd = tmp 
            break
        else:
            index += 1

    lcm = (a * b) / gcd 

    return gcd, lcm


print gcdlcm(3, 20)
