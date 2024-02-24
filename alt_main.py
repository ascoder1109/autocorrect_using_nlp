
import autocorrect_functions

dictionary = autocorrect_functions.load_dictionary("Data/spell-testset1.txt")
input_word = input("Enter an incorrect word: ")
corrected_word = autocorrect_functions.autocorrect_word(input_word,dictionary)
print(f"Corrected Word: {corrected_word}")
