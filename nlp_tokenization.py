import nltk

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

# Define the sentence
sentence = """Tokenization is the process of breaking text into smaller units called tokens.""" 

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence) 
print("Tokens:", tokens) 

# Perform part-of-speech tagging
tagged = nltk.pos_tag(tokens) 
print("POS tagged:", tagged)
