from sklearn.feature_extraction.text import TfidfVectorizer
documents =[
    "i am mariam.",
    "this is a sunny day.",
    "what a day."
]
vectorizer=TfidfVectorizer()
tfidf_matrix=vectorizer.fit_transform(documents)
feature_names=vectorizer.get_feature_names_out()
tfidf_array=tfidf_matrix.toarray()
for i,doc in enumerate(tfidf_array):
    print(f"Document{i+1}")
    for word,score in zip(feature_names,doc):
        print(f"{word} : {score:.4f}")