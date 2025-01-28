def find_smallest_int(arr):
    sn = arr[0]

    for num in arr:
        if num < sn:
            sn = num
    return sn        