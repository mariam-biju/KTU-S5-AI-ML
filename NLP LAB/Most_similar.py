import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('punkt')
def cosine_similarity_manual(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b) if norm_a and norm_b else 0
def find_most_similar_sentence(sentences, input_sentence):
    sentences.append(input_sentence)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences).toarray()
    input_vector = tfidf_matrix[-1]  
    similarities = [
        cosine_similarity_manual(input_vector, tfidf_matrix[i])
        for i in range(len(sentences) - 1)
    ]
    most_similar_index = np.argmax(similarities)
    return sentences[most_similar_index]
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A fast, agile fox leaped over a sleepy canine.",
    "The weather is sunnby and bright today.",
    "I love programming in Python.",
    "Artificial Intelligence is fascinating."
]

input_sentence = input("Enter a sentence: ")
most_similar = find_most_similar_sentence(sentences, input_sentence)
print("Most Similar Sentence:", most_similar)