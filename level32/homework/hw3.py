#Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.

def logical_calc(array, op):
    res = array[0]
    for i in array[1:]:
        if op == 'AND':
            res = res and i
        elif op == 'OR':
            res = res or i
        elif op == 'XOR':
            res = res != i
    return res