import nltk
from nltk import CFG, PCFG, ChartParser, ViterbiParser
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download('punkt')

# Define a more flexible CFG grammar with more general rules
cfg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N | N | Adj N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'man' | 'park' | 'boy' | 'cat' | 'ball' | 'girl' | 'tree'
    V -> 'chased' | 'saw' | 'walked' | 'found' | 'ran'
    Adj -> 'big' | 'small' | 'beautiful' | 'angry' | 'green' | 'quick'
""")

# Define a more flexible PCFG grammar with appropriate probabilities
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.4] | Det Adj N [0.3] | N [0.2] | Adj N [0.1]
    VP -> V NP [0.7] | V [0.3]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'dog' [0.2] | 'cat' [0.2] | 'man' [0.2] | 'park' [0.1] | 'boy' [0.1] | 'ball' [0.1] | 'girl' [0.1]
    V -> 'chased' [0.3] | 'saw' [0.3] | 'walked' [0.2] | 'found' [0.1] | 'ran' [0.1]
    Adj -> 'big' [0.2] | 'small' [0.2] | 'beautiful' [0.2] | 'angry' [0.2] | 'green' [0.1] | 'quick' [0.1]
""")

# Create NLTK parsers
nltk_cfg_parser = ChartParser(cfg_grammar)
nltk_pcfg_parser = ViterbiParser(pcfg_grammar)

# Get user input
text = input("Enter a sentence: ")
tokens = word_tokenize(text.lower())

# 1. NLTK Constituency Parsing
print("\n1. NLTK Constituency Parsing:")
parse_trees = list(nltk_cfg_parser.parse(tokens))
if parse_trees:
    for tree in parse_trees:
        print(tree)
        tree.pretty_print()
else:
    print("No valid constituency parse found.")

# 2. NLTK Probabilistic Parsing
print("\n2. NLTK Probabilistic Parsing:")
parse_trees = list(nltk_pcfg_parser.parse(tokens))
if parse_trees:
    for tree in parse_trees:
        print(tree)
        print(f"Probability: {tree.prob():.6f}")
        tree.pretty_print()
else:
    print("No valid probabilistic parse found.")

