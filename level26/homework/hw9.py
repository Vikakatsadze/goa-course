# ასევე გამოითვალეთ ყველაზე ხშირად რომელი ასაკი გვხვდება

ages = [15,15,16,16,16,16,16,16,15,17,17,17,17,19,21,21,23,25,25,26,32]


first_rank = ages[0]

for element in ages:
    if ages.count(element) > ages.count(first_rank):
       first_rank = element


print(first_rank)
 