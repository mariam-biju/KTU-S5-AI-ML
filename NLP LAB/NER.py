import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
nltk.download('punkt')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')  
sentence=input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)
print(tags)
named_entities = ne_chunk(tags)
print("Named Entities in the sentence:")
for entity in named_entities:
    if isinstance(entity, nltk.Tree):  # Check if it's a named entity (i.e., a subtree)
        print(f"Entity: {' '.join(word for word, tag in entity)} - Type: {entity.label()}")
