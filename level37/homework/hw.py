#გააკეთეთ random student generator რომელსაც გადაეცემა ჯგუფის მოსწავლეებით სავსე სია და დაგვიბრუნებს რენდომულად განაწილებულ გუნდებს მზგავსად როგორც გავაკეთეთ წინა გაკვეთილზე

import random

kutaisi_group50_students = ["გოჩოლეიშვილი", "ცხოვრებაძე", "აპოლო", "ნემსიწვერიძე", "ფანჩულიძე", "ლომინაძე", "სულაქველიძე", "ხარაბაძე", "ძნელაძე"]

all_group = []
squad = []
while kutaisi_group50_students != []:
    if len(kutaisi_group50_students) < 3:
        break
    else:
        for i in range(3):
            random_student = random.choice(kutaisi_group50_students)
            squad.append(random_student)
            kutaisi_group50_students.remove(random_student)

    all_group.append(squad)
    squad = []

for element in all_group:
    print(element)            

