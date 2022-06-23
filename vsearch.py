def search4letters(phrase, letters:str="aeiou") -> set:
     #Display any letters found in an asked-for phrase.
    return set(letters).intersection(set(phrase))


def search4vowels(phrase):
    # Display any vowels found in an asked-for word.
    vowels = set("aeiou")
    return vowels.intersection(set(phrase))
