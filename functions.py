import re
import pattern
# from pattern import 
# from nltk.stem import WordNetLemmatizer

def countingWords(words):
    wordCount = {}
    for word in words:
        if word in wordCount:
            wordCount[word] +=1
        else:
            wordCount[word] = 1
    return wordCount


def probabalityCalculate(wordCountDictionary):
    probablities = {}
    m = sum(wordCountDictionary.values())
    for key in wordCountDictionary.keys():
        probablities[key] = wordCountDictionary[key] / m
    return probablities


def lemmaWord(word):
    return list(pattern.lexmene(wd) for wd in word.split())[0]

def deleteLetter(word):
    deleteList = []
    splitList = []
    for i in range(len(word)):
        splitList.append((word[0:i], word[i:]))
    for a,b in splitList:
        deleteList.append(a+b[1:])
    return deleteList

def switch(word):
    splitList = []
    switchL = []
    for i in range(len(word)):
        splitList.append((word[0:i], word[i:]))
    switchL = [a + b[1] + b[0] + b[2:] for a, b in splitList if len(b) >= 2]
    return switchL


def replace(word):
    splitL = []
    replaceList = []
    for i in range(len(word)):
        splitL.append((word[0:i], word[i:]))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    replaceList = [a + l + (b[1:] if len(b) > 1 else '')
                    for a, b in splitL if b for l in alphabet]
    return replaceList

def insert(word):
    splitL = []
    insertList = []
    for i in range(len(word) + 1):
        splitL.append((word[0:i], word[i:]))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    insertList = [a + l + b for a, b in splitL for l in alphabet]
    return insertList

def colab_1(word, allowSwitches=True):
    colab_1 = set()
    colab_1.update(deleteLetter(word))
    if allowSwitches:
        colab_1.update(switch(word))
    colab_1.update(replace(word))
    colab_1.update(insert(word))
    return colab_1

def colab_2(word, allowSwitches=True):
    colab_2 = set()
    editOne = colab_1(word, allowSwitches=allowSwitches)
    for w in editOne:
        if w:
            editTwo = colab_1(w, allowSwitches=allowSwitches)
            colab_2.update(editTwo)
    return colab_2

def getCorrections(word, probablities, vocab, n=2):
    suggestedWord = []
    bestSuggestion = []
    suggestedWord = list(
        (word in vocab and word) or colab_1(word).intersection(vocab)
        or colab_2(word).intersection(
            vocab))
    bestSuggestion = [[s, probablities[s]] for s in list(reversed(suggestedWord))]
    return bestSuggestion