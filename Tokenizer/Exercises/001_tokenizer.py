print("Hello, AI Engineer!")

sentence = "I love AI"

# TODO:
# 1. Split the sentence into tokens.
# 2. Build a vocabulary.
# 3. Assign integer IDs.
# 4. Convert the sentence to token IDs.
# 5. Convert the IDs back to the original sentence.

# Split the sentence into tokens
sentence = "Hello, AI Engineer! I love AI"
tokens = sentence.split()

# Build a vocabulary
vocabulary = {}

# Assign integer IDs
for token in tokens:
    if token not in vocabulary:
        vocabulary[token] = len(vocabulary)

# Encode
token_ids = []

for token in tokens:
    token_ids.append(vocabulary[token])         

# Decode
decoded_tokens = [list(vocabulary.keys())[list(vocabulary.values()).index(id)] for id in token_ids]

print("Original sentence:", sentence)
print("Tokens:", tokens)
print("Vocabulary:", vocabulary)
print("Token IDs:", token_ids)
print("Decoded tokens:", decoded_tokens)
