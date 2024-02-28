import re
from collections import Counter

def processData(fileName):
    words = []
    with open(fileName) as f:
        fileNameData = f.read()
    fileNameData=fileNameData.lower()
    words = re.findall(r'\w+',fileNameData)
    return words

wordList = processData("Data/big.txt")
vocabulary = set(wordList)

def getCount(wordList):
    wordCountDictionary = {}
    wordCountDictionary = Counter(wordList)
    return wordCountDictionary

wordCountDictionary = getCount(wordList)

def deleteLetter(word):
    deleteList = []
    splitList = []
    for i in range (len(word)):
        splitList.append([word[:i], word[i:]])
    for a,b in splitList:
        deleteList.append(a+b[1:])
    return deleteList

def replaceLetter(word):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    replaceList = []
    splitList = []
    for c in range (len(word)):
        splitList.append((word[0:c],word[c:]))
    replaceList = [a+l+(b[1:] if len(b)>1 else '') for a,b in splitList if b for l in letter]
    replaceSet = set(replaceList)
    replaceSet.remove(word)
    return replaceList

def insertLetter(word):
        letter = 'abcdefghijklmnopqrstuvwxyz'
        insertList = []
        splitList = []
        for c in range (len(word)+1):
            splitList.append((word[0:c],word[c:]))
        insertList = [a+l+b for a,b in splitList for l in letter]
        return insertList
    
def getProbablity(wordCountDictionary):
    probablities = {}
    m = sum(wordCountDictionary.values())
    for key in wordCountDictionary:
        probablities[key] = wordCountDictionary[key]/m
    return probablities

probablity = getProbablity(wordCountDictionary)

def switchLetter(word):
    splitList = []
    switchL = []
    for i in range(len(word)):
        splitList.append((word[0:i], word[i:]))
    switchL = [a + b[1] + b[0] + b[2:] for a, b in splitList if len(b) >= 2]
    return switchL

def editOneLetter(word, allowSwitches = True):
    editOneSet = set()
    editOneSet.update(deleteLetter(word))
    if allowSwitches:
        editOneSet.update(switchLetter(word))
        
    editOneSet.update(replaceLetter(word))
    editOneSet.update(insertLetter(word))
    
    return editOneSet

def editTwoLetters(word,allowSwitches = True):
    editTwoSet = set()
    editOne = editOneLetter(word,allowSwitches=allowSwitches)
    for w in editOne:
        if w:
            editTwo = editOneLetter(w,allowSwitches=allowSwitches)
            editTwoSet.update(editTwo)
    return editTwoSet

def getCorrections(word, probablity, vocabulary):
    suggestion = []
    n_best = []
    suggestions = list((word in vocabulary and word) or editOneLetter(word).intersection(vocabulary) or editTwoLetters(word).intersection(vocabulary))
    n_best = [[s,probablity[s]] for s in list(reversed(suggestions))]
    return n_best
