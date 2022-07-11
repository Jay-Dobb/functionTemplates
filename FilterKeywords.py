# filter out  Keywords from 2 List joined


fruitbag = ['Apps', 'Bans', 'Chers', 'Keys', 'Mans', 'Apps2', 'Guav']

fruitsdescription = ['apples texture', 'banana ghost', 'cherry pops', 'kiwi hunter', 'mango chooser',
                     'apple sauce fresh', 'guava man two']

filters = ['apple', 'grape', 'blueberry', 'kiwi']

newlistcombined = []

for x,z in zip(fruitsdescription,fruitbag):
    if any(w in x for w in filters):
        print('found and removed', 'index: ', fruitsdescription.index(x))

    else:
        newlistcombined.append([z, x])

print(newlistcombined, "\n")

for x in newlistcombined:
    print("Title: ", x[0], "Body Desc: ", x[1])


print('\n ---------------------------------------------------------- \n ')

occurenceList = []
title = ['SL C ','FS D ','FS H','FS F','FS D','SL C','SL F','FS H','SL H','SL D']
mama = ['slow cat Sas','fast dog PoP','fast hen Luke','fast fish Lee','fast dog joe','slow cat yan','slow fish ben','Fast hen Tim','Slow hen Jen','slow dog moe']
filterkeywords = ['hen','dog','Fish']

for text in mama:
   index = (mama.index(text))
   print(index,text," ",title[index])

print(" ")

for text in title:
   index = (title.index(text))
   print(index,text)

print(" ")


for words in filterkeywords:
   occurences = sum(x.count(words) for x in mama)
   if occurences > 0:
      occurenceAmt = sum(x.count(words) for x in mama)
      occurenceDetails = str(occurenceAmt) + ' Occurences For:' + words
      occurenceList.append(occurenceDetails)

occurenceList.sort(reverse=True)
for item in occurenceList:
   print(item)


print(" ")
for text in mama:
   for words in filterkeywords:
      if words in text:
         animal = (mama.index(text))
         print("index: ", animal, ' | ', mama[animal], " | Word Found: ", words)


this = [f'{t}' for i,(t, m) in enumerate(zip(title, mama)) if not any(w in m for w in filterkeywords)]

for items in this:
   print(items)

print(this)