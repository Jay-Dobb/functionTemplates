#bigger concept would be for webscraping online sites with duplicate titles but different attributes

NamesFromForum = ['Jay', 'Boon', 'Jay', 'Sue', 'Tim', 'Lia', 'Lia', 'John', 'John', 'Abe']
AgesFromForum = [20, 40, 30, 26, 28, 21, 18, 91, 10, 25]
LocFromForum = ['BA', 'CA', 'NM', 'CO', 'AL', 'NY', 'TX', 'NV', 'MN', 'SO']

NameNoDup = []
ageAlignName = []
LocAlignName = []
Combinedlist = []

def listextract():
    nameSet = set()

    for name, age, loc in zip(NamesFromForum, AgesFromForum, LocFromForum):
        if name not in nameSet:
            NameNoDup.append(name)
            ageAlignName.append(age)
            LocAlignName.append(loc)
            nameSet.add(name)

            Combined = name + " | Age: " + str(age) + " | Location: " + loc
            Combinedlist.append(Combined)

def printlist():
    item = 0
    print(NameNoDup)
    print(ageAlignName)
    print(LocAlignName)
    print(" ")

    with open('readme.txt', 'w') as f:
        for x in Combinedlist:
            f.write(str(NameNoDup[item]) + str(ageAlignName[item]))
            f.write('\n')
            f.write(" ------------------------------------------------- ")
            f.write('\n')
            f.write('\n')
            print(Combinedlist[item])
            item = item + 1

    skimBody = (NameNoDup[1])
    print(skimBody[0:1])
    print(len(NameNoDup))

listextract()
printlist()


