import spacy

# Load the language model
nlp = spacy.load("en_core_web_md")

while True:
    # Get user input
    user_word = input("Enter a word: ")

    # Process the word
    doc = nlp(user_word)

    # Check if correction needed
    if doc[0].text != doc[0].norm:
        # Use spaCy's contextual spellchecker for suggestions
        corrected_word = nlp(user_word)._.spellcheck[0].text

        # Print the correction with optional score or explanation
        print(f"Possible correction: {corrected_word}")

        # Optionally print explanation using explain() (requires spaCy>=3.3.0)
        if spacy.__version__ >= "3.3.0":
            print(nlp(user_word).explain(corrected_word))

    else:
        print("The word is already spelled correctly!")

    # Ask if user wants to continue
    if input("Continue? (y/n) ").lower() != "y":
        break
