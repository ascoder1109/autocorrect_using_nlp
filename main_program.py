import functions_program

myWord = input("Enter a word:")
temporaryCorrections = functions_program.getCorrections(myWord,functions_program.probablity,functions_program.vocabulary)
temporaryCorrections.sort(key=lambda x: x[1], reverse=True)


for i, (word, probability) in enumerate(temporaryCorrections):
    print(f"word {i}: {word}")