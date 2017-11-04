# Karatsuba Multiplication
# Input: n digits two integers. n is a power of 2
# Output: Multiplied resutl of the input numbers

# Psedocodes
# x*y = 10-to-n * ac + 10-to-n/2 * (ad+bc) + bd
# a = x / 10-to-n/2 b = x % 10-to-n/2
# c = y / 10-to-n/2 d = y % 10-to-n/2
# step 1. recursively compute ac
# step 2. recursively compute bd
# step 3. recursively compute (a+b)(c+d) = ac + ad + bc + bd
# Gauss' trick: 3 - 1 -2 = ad + bc

def karatsuba(x, y):
    # Find n
    n1 = len(str(x))
    n2 = len(str(y))
    n = min(n1, n2)
    
    # Just checking of x digits, sufficient enough?
    # Yes, this case will only happen with step 3,
    # only when n = 1
    if n == 1:
        return x * y
    
    n = max(n1, n2)
    m = int(n/2)
    
    a = int(x / (10**m))
    b = int(x % (10**m))
    c = int(y / (10**m))
    d = int(y % (10**m))
    
    # step 1
    ac = karatsuba(a, c)
    
    # step 2
    bd = karatsuba(b, d)
    
    # step 3
    adbc_temp = karatsuba(a+b, c+d)
    
    adbc = adbc_temp - ac - bd
    
    result = int((10**(2*m))*ac) + int((10**m)*adbc) + int(bd)
    return result

# This implentation fails with these large numbers.
# To be debugged.
#x = 3141592653589793238462643383279502884197169399375105820974944592
#y = 2718281828459045235360287471352662497757247093699959574966967627

x = 3141592653589793238462643383279502 #8#8 #4197169 #399375105820974944592
y = 2718281828459045235360287471352662 #4#9 #7757247 #093699959574966967627

res1 = karatsuba(x, y)
res2 = x * y

if res1 == res2:
    print("Result matching.")
else:
    print("Result not matching.")
    
print("res1", res1)
print("res2", res2)
