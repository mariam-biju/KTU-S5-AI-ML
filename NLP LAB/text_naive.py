import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

class TextClassifier:
    def __init__(self):
        # Hardcoded dataset
        data = {
            "text": [
                "I love this product, it is amazing!",
                "This is the worst experience I have ever had.",
                "The service was okay, nothing special.",
                "Absolutely fantastic! Highly recommend it.",
                "Terrible, I will never buy this again.",
                "It was decent, but could be better.",
                "I am very satisfied with the quality.",
                "The product broke after one use, very disappointed.",
                "Great value for the price, I am happy with it.",
                "Not worth the money, very poor quality."
            ],
            "sentiment": [
                "positive", "negative", "neutral", "positive", "negative",
                "neutral", "positive", "negative", "positive", "negative"
            ]
        }
        self.data = pd.DataFrame(data)  # Create a DataFrame from the hardcoded data
        self.vectorizer = TfidfVectorizer()  # For converting text to numerical features
        self.model = MultinomialNB()  # Naive Bayes classifier

    def preprocess_data(self):
        """
        Preprocess the datatgset by splitting it into training and testing sets.
        """
        X = self.data['text']  # Text data
        y = self.data['sentiment']  # Labels

        # Split the data into training and testing sets (80% train, 20% test)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    def train_model(self):
        """
        Train the text classification model using Naive Bayes.
        """
        # Convert text data to numerical features using TF-IDF
        X_train_tfidf = self.vectorizer.fit_transform(self.X_train)
        X_test_tfidf = self.vectorizer.transform(self.X_test)

        # Train the Naive Bayes classifier
        self.model.fit(X_train_tfidf, self.y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test_tfidf)
        print("Accuracy:", accuracy_score(self.y_test, y_pred))
        print("\nClassification Report:\n", classification_report(self.y_test, y_pred))

    def classify_text(self, text):
        """
        Classify new text input using the trained Naive Bayes model.
        """
        # Convert the input text to numerical features
        text_tfidf = self.vectorizer.transform([text])
        # Predict the label
        prediction = self.model.predict(text_tfidf)
        return prediction[0]

def main():
    print("Welcome to the Naive Bayes-Based Text Classifier!")
   
    # Initialize and preprocess the classifier
    classifier = TextClassifier()
    classifier.preprocess_data()
   
    # Train the model
    print("Training the model...")
    classifier.train_model()
   
    # Test the classifier with user input
    while True:
        user_input = input("\nEnter a sentence (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        prediction = classifier.classify_text(user_input)
        print(f"Predicted Sentiment: {prediction}")

if __name__ == "__main__":
    main()