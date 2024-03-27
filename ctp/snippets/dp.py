### Ex. 1 Dynamic Programming

def test_multiplication_dp(n, m, d, expected):
    result = multiplication_dp(n, m, d)
    if expected == result:
        return True
    else:
        return False
# Code of the function
def multiplication_dp(n, m, d):
# Checking if a solution exists
    if n * m not in d:
        if m == 0 or n == 0: # base case 
            d[n * m] = 0 
        else: # recursive step
        # the dictionary will be passed as input of the recursive
        # calls of the function
            d[n * m] = n + multiplication_dp(n, m - 1, d)
    return d.get(n * m)

empty_dic = {}

#tests
print(test_multiplication_dp(3, 5, empty_dic, 15))
print(test_multiplication_dp(-1, 7, empty_dic, -7))
print(test_multiplication_dp(20, 50, empty_dic, 1000))
print(test_multiplication_dp(-17, -5, empty_dic, 85))
print(test_multiplication_dp(0, 0, empty_dic, 0))
print(test_multiplication_dp(1, 1, empty_dic, 1))

### Ex. 2 Dynamic Programming

def test_exponentiation_dp(n, m, d, expected):
    result = exponentiation_dp(n, m, d)
    if expected == result:
        return True
    else:
        return False

def exponentiation_dp(n, e, d):

    if n ** e not in d:
        if e == 0:
            d[n ** e] = 1
        elif e > 0:
            d[n ** e] = n * exponentiation_dp(n, e - 1, d)
        else:
            d[n ** e] = 1/n * exponentiation_dp(n, e + 1, d)  

    return d.get(n ** e)


#tests
print(test_exponentiation_dp(1, 1, empty_dic, 1))
print(test_exponentiation_dp(2, 3, empty_dic, 8))
print(test_exponentiation_dp(-3, 4, empty_dic, 81))
print(test_exponentiation_dp(9, -1, empty_dic, 1/9))
print(test_exponentiation_dp(3, -3, empty_dic, 1/27))
print(test_exponentiation_dp(-3, -2, empty_dic,1/9))
print(test_exponentiation_dp(2, -4, empty_dic, 1/16))
print(test_exponentiation_dp(0, 4, empty_dic, 0))

