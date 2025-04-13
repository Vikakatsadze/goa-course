def number_of_duplicate_digits(ndigit):
    start = 10**(ndigit-1)
    end = 10**ndigit
    count = 0
    if ndigit <10:
        return 0
    else:
        for num in range(start, end):
            string = str(num)
            for i in range(len(string)-1):
                if string[i] == string[i+1]:
                    count += 1
                    break