#You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    sum = 0
    for elements in arr:
        if elements > 0:
            sum += elements
    return sum        