import functions_program

myWord = input("Enter a word:")
temporaryCorrections = functions_program.getCorrections(myWord,functions_program.probablity,functions_program.vocabulary,2)
for i,wordProbablity in enumerate(temporaryCorrections):
    print(f"word {i}: {wordProbablity[0]}       probablity:{wordProbablity[1]:.6f}")