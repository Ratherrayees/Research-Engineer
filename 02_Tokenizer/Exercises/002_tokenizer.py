# 002_tokenizer.py

# TODO:
# 1. Split the sentence into tokens.
# 2. Build a vocabulary.
# 3. Assign integer IDs.
# 4. Convert the sentence to token IDs.
# 5. Convert the IDs back to the original sentence.
# 6. Reconstruct the original sentence instead of stopping at tokens.
# 7. Create reverse vocabulary once, instead of searching through the vocuabulary each time.

# Split the sentence into tokens
sentence = "Hello, AI Engineer! I love AI, and I am excited to learn more about AI."
tokens = sentence.split()

# Build a vocabulary
vocabulary = {}

# Assign integer IDs
for token in tokens:
    if token not in vocabulary:
        vocabulary[token] = len(vocabulary)

# Create reverse vocabulary once, instead of searching through the vocabulary each time
reverse_vocabulary = {id: token for token, id in vocabulary.items()}

# Encode
token_ids = []

for token in tokens:
    token_ids.append(vocabulary[token])         

# Decode
decoded_tokens = [reverse_vocabulary[id] for id in token_ids]

# Reconstruct the original sentence
reconstructed_sentence = ' '.join(decoded_tokens)

print("Original sentence:", sentence)
print("Tokens:", tokens)
print("Vocabulary:", vocabulary)
print("Token IDs:", token_ids)
print("Decoded tokens:", decoded_tokens)
print("Reconstructed sentence:", reconstructed_sentence)
print("Reverse vocabulary:", reverse_vocabulary)
