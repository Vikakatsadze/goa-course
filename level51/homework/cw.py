def array_diff(a, b):
    List = []
    for num in a:
        if num not in b:
            List.append(num)
    return List