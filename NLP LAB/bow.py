from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
def compute_cosine_similarity_manual(matrix):
    num_rows = matrix.shape[0]
    similarity_matrix = np.zeros((num_rows, num_rows))
    
    for i in range(num_rows):
        for j in range(num_rows):
            vector_a = matrix[i].toarray()[0]
            vector_b = matrix[j].toarray()[0]
            dot_product = np.dot(vector_a, vector_b)
            norm_a = np.linalg.norm(vector_a)
            norm_b = np.linalg.norm(vector_b)
            similarity_matrix[i][j] = dot_product / (norm_a * norm_b) if norm_a and norm_b else 0
    return similarity_matrix
def create_bow_and_compute_similarity(documents):
    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(documents)
    similarity_matrix = compute_cosine_similarity_manual(bow_matrix)
    return bow_matrix, similarity_matrix
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]
bow_matrix, similarity_matrix = create_bow_and_compute_similarity(documents)
print("Bag of Words Matrix:\n", bow_matrix.toarray())
print("\nCosine Similarity Matrix:\n", similarity_matrix)
















'''from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def create_bow_and_compute_similarity(documents):
    # Create a CountVectorizer object to convert text documents to a matrix of token counts
    vectorizer = CountVectorizer()
    # Fit the model and transform the documents into a bag-of-words representation
    bow_matrix = vectorizer.fit_transform(documents)
    # Compute the cosine similarity matrix from the bag-of-words matrix
    similarity_matrix = cosine_similarity(bow_matrix)
    return bow_matrix,similarity_matrix
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]
bow_matrix, similarity_matrix = create_bow_and_compute_similarity(documents)
print("Bag of Words Matrix:",bow_matrix.toarray())
print("Cosine Similarity Matrix:", similarity_matrix)'''