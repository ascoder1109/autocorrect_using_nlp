import functions_program

myWord = input("Enter a word:")
temporaryCorrections = functions_program.getCorrections(myWord,functions_program.probablity,functions_program.vocabulary,2)
# for i,wordProbablity in enumerate(temporaryCorrections):
#     print(f"word {i}: {wordProbablity[0]}       probablity:{wordProbablity[1]:.6f}")
    
temporaryCorrections.sort(key=lambda x: x[1], reverse=True)

for i, wordProbablity in enumerate(temporaryCorrections):
    probability_percentage = wordProbablity[1] * 1000000  # Convert to percentage
    print(f"word {i}: {wordProbablity[0]}   probablity: {probability_percentage:.2f}%")
