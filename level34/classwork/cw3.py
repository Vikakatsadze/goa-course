#The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

def century(year):
    return int(year + 99) // 100

# 2 ვარიანტი

#def century(year):
     #if year % 100 == 0:
        #return year // 100:
     #else:
        #return (year // 100) + 1