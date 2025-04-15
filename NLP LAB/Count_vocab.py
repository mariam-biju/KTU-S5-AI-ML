text = """
The quick brown fox jumps over the lazy dog. 
Natural Language Processing is fascinating. 
Machine learning and deep learning are subsets of artificial intelligence.
The river bank is beautiful, and the bank has been robbed.
"""
text = text.lower()
valid_char = "abcdefghijklmnopqrstuvwxyz1234567890"
cleaned_text = ''.join(char if char in valid_char + ' ' else ' ' for char in text)
tokens = cleaned_text.split()
num_tokens = len(tokens)
distinct = set(tokens)
num_types = len(distinct)
freq = {}
for token in tokens:
    if token in freq:
        freq[token] += 1
    else:
        freq[token] = 1
ttr = (num_types / num_tokens) * 100 if num_tokens > 0 else 0
print("Number of tokens:", num_tokens)
print("Number of types of words:", num_types)
sorted_freq = dict(sorted(freq.items()))
print("Frequency of tokens:")
for word, frequency in sorted_freq.items():
    percentage = (frequency / num_tokens) * 100
    print(f"{word}: {frequency} ({percentage:.2f}%)")
print(f"Type-Token Ratio: {ttr:.2f}%")