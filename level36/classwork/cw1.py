import random



goa_group50_students = ['ცხადაძე', 'სოფია', 'ხუციშვილი', 'ჯანხოთელი', 'ბაღათურია', 'ბოკუჩავა', 'ანა', 'გლოველი', 'ბერაშვილი', 'სამსონიძე', 'გოგა', 'დაჩი გიორგაძე', 'კესარია ჩიჩუა', 'მერუმოვი', 'ნიკა აბულაძე', 'კაცაძე']

all_group = []  #აქ შეინახება ყველა გუნდი
squad = []  # აქ არის ერთი გუნდი რომელიც იტრიალებს
while goa_group50_students != []: #სანამ ჩვენი სია არიქნება ცარიელი მანამდე შესრულდება ეს ყველაფერი

    if len(goa_group50_students) < 3: #თუ ჩვენი სიის სიგრძე იქნება < 3 ზე
        break #მაშინ აქ შეჩერდება და აღარ გაგრძელდება
    else: #ხოლო სხვა შემთხვევაში
        for i in range(3): #დავატრიალებთ ციკლს სამჯერ გვჭირდება სამი მოსწავლე
            random_student = random.choice(goa_group50_students)#რენდომ მოსაწვლეს ვირჩევთ და დაემატება squad-ში
            squad.append(random_student)
            goa_group50_students.remove(random_student)#შემდეგ სიიდან წაიშლება რაც დაემატება squad - ში ის წაიშლება თან სიიდან

    all_group.append(squad) # შემდეგ all groups დაემატება squad-ში შესული მოსწავლეები და ჩვენი ეს squad დაცარიელდება
    squad = []

for element in all_group: #მივწვედებით ამ სიის თითოეულ ელემენტს
    print(element)
print(goa_group50_students)  #და დავბეჭდავთ  