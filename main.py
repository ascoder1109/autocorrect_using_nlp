import re
import functions
w = []
with open('Data/biggest.txt','r',encoding="utf") as f:
    fileName = f.read()
    fileName = fileName.lower()
    w = re.findall('\w+',fileName)

mainSet = set(w)

myWord = input("Enter any word:")
wordCount = functions.countingWords(mainSet)
probablities = functions.probabalityCalculate(wordCount)
temporaryCorrections = functions.getCorrections(myWord,probablities,mainSet,2)
for i, word_prob in enumerate(temporaryCorrections):
    if(i < 3):
        print(word_prob[0])
    else:
        break