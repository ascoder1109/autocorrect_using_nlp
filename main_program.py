import functions_program

myWord = input("Enter a word:")
temporaryCorrections = functions_program.getCorrections(myWord,functions_program.probablity,functions_program.vocabulary,2)
# for i,wordProbablity in enumerate(temporaryCorrections):
#     print(f"word {i}: {wordProbablity[0]}       probablity:{wordProbablity[1]:.6f}")
    
temporaryCorrections.sort(key=lambda x: x[1], reverse=True)
# d
# print(temporaryCorrections)

for i, (word, probability) in enumerate(temporaryCorrections):
    # Ensure probability is between 0 and 100
    probability_percentage = min(100, probability * 1000000)
    print(f"word {i}: {word}  accuracy: {probability_percentage:.2f}%")