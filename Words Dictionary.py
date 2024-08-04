from PyDictionary import PyDictionary

print("==============================")
title = "Words Dictionary".upper()
print(title.center(30, "="))
print("==============================")

def print_meaning(word):
    meanings = dictionary.meaning(word)
    if meanings:
        for part_of_speech, definitions in meanings.items():
            print(f"{part_of_speech}:")
            for definition in definitions:
                print(f"  - {definition}")
    else:
        print("No meaning found for this word.")

def print_synonyms(word):
    synonyms = dictionary.synonym(word)
    if synonyms:
        print("Synonyms:")
        for synonym in synonyms:
            print(f"  - {synonym}")
    else:
        print("No synonyms found for this word.")
        print(".............................")

def print_antonyms(word):
    antonyms = dictionary.antonym(word)
    if antonyms:
        print("Antonyms:")
        for antonym in antonyms:
            print(f"  - {antonym}")
    else:
        print("No antonyms found for this word.")
        print(".............................")

dictionary = PyDictionary()

while True:
    word = input("\nEnter a word (or press Enter to exit): ").lower().strip()
    if word == "":
        print("Closing dictionary. Goodbye!")
        break
    
    print(f"\nLooking up the word: {word}")
    
    print("\nMeaning:")
    print_meaning(word)
    print(".............................")
    
    print("\nSynonyms:")
    print_synonyms(word)
    print(".............................")
    
    print("\nAntonyms:")
    print_antonyms(word)
    print(".............................")
