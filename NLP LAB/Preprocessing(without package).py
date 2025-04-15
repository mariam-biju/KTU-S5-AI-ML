stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'}

punctuation = "!?()[]{};:'\"\\,<>./?@#$%^&*_~`-=+|\\"

def expand_contractions(tweet):
    contractions_dict = {
        "i'm": "i am", "you're": "you are", "he's": "he is", "she's": "she is", "it's": "it is",
        "we're": "we are", "they're": "they are", "i've": "i have", "you've": "you have", "we've": "we have",
        "they've": "they have", "i'd": "i would", "you'd": "you would", "he'd": "he would", "she'd": "she would",
        "we'd": "we would", "they'd": "they would", "i'll": "i will", "you'll": "you will", "he'll": "he will",
        "she'll": "she will", "we'll": "we will", "they'll": "they will", "isn't": "is not", "aren't": "are not",
        "wasn't": "was not", "weren't": "were not", "haven't": "have not", "hasn't": "has not", "didn't": "did not",
        "don't": "do not", "doesn't": "does not", "can't": "cannot", "couldn't": "could not", "won't": "will not",
        "wouldn't": "would not", "shouldn't": "should not", "mustn't": "must not", "needn't": "need not", "let's": "let us",
        "that's": "that is", "what's": "what is", "who's": "who is", "where's": "where is", "how's": "how is",
        "here's": "here is", "there's": "there is"
    }
    for contraction, expanded in contractions_dict.items():
        tweet = tweet.replace(contraction, expanded)
    return tweet

def preprocess_tweet(tweet):
    tweet_lower = tweet.lower()
    print(f"After Lowercase: {tweet_lower}")
    
    sentence = tweet_lower.split('.')
    print(f"After Sentence Tokenization: {sentence}")
    
    tweet_no_urls = ''
    for word in tweet_lower.split():
        if not word.startswith("http://") and not word.startswith("https://") and not word.startswith("www."):
            tweet_no_urls += word + ' '
    print(f"After URL Removal: {tweet_no_urls}")

    tweet_no_emojis = ''.join(char for char in tweet_no_urls if ord(char) < 128)
    print(f"After Emoji Removal: {tweet_no_emojis}")
    
    tweet_no_contractions = expand_contractions(tweet_no_emojis)
    print(f"After Expanding Contractions: {tweet_no_contractions}")
    
    tweet_no_punctuation = ''.join(char for char in tweet_no_contractions if char not in punctuation)
    print(f"After Punctuation Removal: {tweet_no_punctuation}")
   
    tokens = tweet_no_punctuation.split()
    print(f"After Word Tokenization: {tokens}")

    tokens_no_stopwords = [word for word in tokens if word not in stop_words]
    print(f"After Stopword Removal: {' '.join(tokens_no_stopwords)}")

    tokens_stemmed = [word[:-1] if word.endswith('s') else word for word in tokens_no_stopwords]
    print(f"After Stemming: {' '.join(tokens_stemmed)}")

    tokens_lemmatized = [word[:-3] if word.endswith('ing') else word[:-2] if word.endswith('ed') else word for word in tokens_no_stopwords]
    print(f"After Lemmatization: {' '.join(tokens_lemmatized)}")

    cleaned_tweet = ' '.join(tokens_lemmatized)
    print(f"Final Processed Tweet: {cleaned_tweet}")
    print("-----")
    
    return cleaned_tweet

def read_tweets_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tweets = file.readlines()
    return [tweet.strip() for tweet in tweets]  

file_path = 'tweets.txt'
tweets = read_tweets_from_file(file_path)

cleaned_tweets = [preprocess_tweet(tweet) for tweet in tweets]

for i, tweet in enumerate(cleaned_tweets):
    print(f"Original Tweet: {tweets[i]}")
    print(f"Processed Tweet: {tweet}")

