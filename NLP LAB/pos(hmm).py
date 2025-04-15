import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import treebank
from nltk.tag import hmm
from nltk.probability import LaplaceProbDist

# Define a dictionary for expanded tag names
tag_expansion = {
    'CC': 'Coordinating Conjunction',
    'CD': 'Cardinal Digit',
    'DT': 'Determiner',
    'EX': 'Existential There',
    'FW': 'Foreign Word',
    'IN': 'Preposition/Subordinating Conjunction',
    'JJ': 'Adjective',
    'JJR': 'Adjective, Comparative',
    'JJS': 'Adjective, Superlative',
    'LS': 'List Item Marker',
    'MD': 'Modal',
    'NN': 'Noun, Singular',
    'NNS': 'Noun, Plural',
    'NNP': 'Proper Noun, Singular',
    'NNPS': 'Proper Noun, Plural',
    'PDT': 'Predeterminer',
    'POS': 'Possessive Ending',
    'PRP': 'Personal Pronoun',
    'PRP$': 'Possessive Pronoun',
    'RB': 'Adverb',
    'RBR': 'Adverb, Comparative',
    'RBS': 'Adverb, Superlative',
    'RP': 'Particle',
    'SYM': 'Symbol',
    'TO': 'To',
    'UH': 'Interjection',
    'VB': 'Verb, Base Form',
    'VBD': 'Verb, Past Tense',
    'VBG': 'Verb, Gerund or Present Participle',
    'VBN': 'Verb, Past Participle',
    'VBP': 'Verb, Non-3rd Person Singular Present',
    'VBZ': 'Verb, 3rd Person Singular Present',
    'WDT': 'Wh-determiner',
    'WP': 'Wh-pronoun',
    'WP$': 'Possessive Wh-pronoun',
    'WRB': 'Wh-adverb'
}

def expand_tag(tag):		# Function to expand the tag
    return tag_expansion.get(tag, "Unknown Tag")

text = input("Enter a sentence: ")		# Word tokenization
tokens = nltk.word_tokenize(text)
print("Tokens:", tokens)

lemmatizer = WordNetLemmatizer()		# Lemmatization
l_tokens = [lemmatizer.lemmatize(token) for token in tokens]
print("Lemmatized tokens:", l_tokens)

from nltk import pos_tag			# POS tagging using NLTK's built-in pos_tag

pos_tags = pos_tag(l_tokens)
print("\nPOS tags for the sentence:")
for l_token, tag in pos_tags:
    expanded_tag = expand_tag(tag)
    print(f"{l_token}: {tag} ({expanded_tag})") 

						# Train the HMM POS Tagger using Treebank corpus
train_sents = treebank.tagged_sents()[:4000]  	# First 3000 sentences for training
test_sents = treebank.tagged_sents()[4000:]  	# Remaining sentences for testing
					
trainer = hmm.HiddenMarkovModelTrainer()	# Train the HMM POS Tagger
hmm_tagger = trainer.train(train_sents, estimator=LaplaceProbDist)	 # Use Laplace smoothing

tags = hmm_tagger.tag(l_tokens)			# Use the trained tagger on the lemmatized tokens

print("\nPOS tags for the lemmatized sentence using HMM tagger:")
for l_token, tag in tags:
    expanded_tag = expand_tag(tag)
    print(f"{l_token}: {tag} ({expanded_tag})")  
    
