sentences=['The stupid boy', '3.4', 'How can I be this stupid']

def find_sentences_with_words(lst):
    return [value for value in lst if value.isalpha()]

print(find_sentences_with_words(sentences))



