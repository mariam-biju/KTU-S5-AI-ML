import nltk
from nltk.text import Text

# Download necessary NLTK resources
nltk.download('punkt')

# Hardcoded text
text = """
The quick brown fox jumps over the lazy dog. 
The bank has been robbed.
AI is an interesting topic.
The river bank is beautiful.
"""

# Tokenize the text (no preprocessing)
tokens = nltk.word_tokenize(text)

# Create a Text object for concordance search
obj = Text(tokens)

# Read the word to be searched from the user
target = input("Enter the word to search: ")

# Perform concordance search
print(f"\nConcordance for the word '{target}':")
obj.concordance(target, width=80)












'''import nltk
from nltk.text import Text
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Hardcoded text
text = """
The quick brown fox jumps over the lazy dog. 
The bank has been robbed.
AI is an interesting topic.
The river bank is beautiful.
"""

# Convert text to lowercase and remove punctuation
text_no_punctuation = ''.join(char.lower() if char not in string.punctuation else ' ' for char in text)

# Tokenize the text
tokens = nltk.word_tokenize(text_no_punctuation)

# Remove stopwords
stopwords = set(nltk.corpus.stopwords.words('english'))
words_no_stopwords = [word for word in tokens if word not in stopwords]

# Create a Text object for concordance search
obj = Text(words_no_stopwords)

# Search for a word in the text
target = input("Enter the word to search: ").lower()
print(f"\nConcordance for the word '{target}':")
obj.concordance(target, width=80)
'''