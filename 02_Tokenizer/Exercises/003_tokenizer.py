# 003_tokenizer.py

# TODO:

# 1. Corpus
# 2. Break into tiny units
# 3. Count neighboring pairs
# 4. Find most frequent pair
# 5. Merge that pair everywhere
# 6. Add merged piece to vocabulary
# 7. Repeat

# Corpus
corpus = "Hello, AI Engineer! I love AI, and I am excited to learn more about AI. " \
"this is a test sentence for the tokenizer exercise. The tokenizer will break this sentence into tokens, build a vocabulary, and assign integer IDs to each token. It will then convert the sentence to token IDs and reconstruct the original sentence from those IDs. " \
"count neighboring pairs of tokens, find the most frequent pair, merge that pair everywhere in the corpus, and add the merged piece to the vocabulary. This process will be repeated until a certain condition is met, such as reaching a maximum vocabulary size or a minimum frequency threshold for merging pairs. " \
"also handle special cases, such as punctuation, whitespace, and case sensitivity. It will ensure that the tokens are properly normalized and that the vocabulary is built in a consistent manner. The final output will include the original corpus, the list of tokens, the vocabulary with assigned integer IDs, the token IDs for the original corpus, and the reconstructed corpus from those IDs. " \
"provide insights into the frequency of tokens and pairs, allowing for analysis of the corpus and the effectiveness of the tokenization process. It will also allow for customization of the tokenization rules, such as defining specific delimiters or handling special characters. The tokenizer will be designed to be efficient and scalable, capable of processing large corpora in a reasonable amount of time. " \
"include error handling and validation to ensure that the input corpus is valid and that the tokenization process is robust. It will provide clear error messages and guidance for resolving any issues that may arise during tokenization. The tokenizer will also include unit tests to verify the correctness of its functionality and to ensure that it meets the specified requirements. " \
"documentation and examples to help users understand how to use the tokenizer effectively. It will provide guidance on how to customize the tokenization process and how to interpret the output. The tokenizer will be designed to be user-friendly and accessible, with clear instructions and examples for users of all skill levels. " \
"performance metrics and benchmarks to evaluate its efficiency and scalability. It will provide insights into the time and space complexity of the tokenization process, allowing users to make informed decisions about its use in different scenarios. The tokenizer will be designed to be modular and extensible, allowing for easy integration with other tools and systems. "
"now about the common words and similar words and words which add more character to form new words are: learn, learnable, learning, learned, learner, learnings, learnability, learnable, learnably, learnableness,"

# split corpus into words.
words = corpus.split()

# split words into characters
characters = [list(word) for word in words]

# count neighboring pairs inside every inner list.
pair_counts = {}
for char_list in characters:
    for i in range(len(char_list) - 1):
        pair = (char_list[i], char_list[i + 1])
        pair_counts[pair] = pair_counts.get(pair, 0) + 1

# find the pair with the highest count.
most_common_pair = max(pair_counts, key=pair_counts.get)

# Start rounds of merging pairs
rounds = 1
max_rounds = 500

# create merger rules
merge_rules = []

# merge that pair everywhere it appears, while keeping each word separate.
while True:
    # Add the merged pair to the new merger rules
    merge_rules.append(most_common_pair)
    # Observe a fixed number of merge rounds and print what happens each round.
    print(f"Round: {rounds}, Most Common Pair: {most_common_pair}")
    new_characters = []
    for char_list in characters:
        new_char_list = []
        i = 0
        while i < len(char_list):
            if i < len(char_list) - 1 and (char_list[i], char_list[i + 1]) == most_common_pair:
                new_char_list.append(''.join(most_common_pair))
                i += 2
            else:
                new_char_list.append(char_list[i])
                i += 1
        new_characters.append(new_char_list)
    
    # Update characters with the new merged characters
    characters = new_characters
    
    # Recount neighboring pairs
    pair_counts = {}
    for char_list in characters:
        for i in range(len(char_list) - 1):
            pair = (char_list[i], char_list[i + 1])
            pair_counts[pair] = pair_counts.get(pair, 0) + 1
    
    # Find the next most common pair
    if not pair_counts:
        break
    most_common_pair = max(pair_counts, key=pair_counts.get)
    if rounds >= max_rounds:
        break
    rounds += 1

# Build a vocabulary from the final characters
vocabulary = {}
for char_list in characters:
    for char in char_list:
        if char not in vocabulary:
            vocabulary[char] = len(vocabulary)

# encode the final token pieces into their IDs.
token_ids = []
for char_list in characters:
    for char in char_list:
        token_ids.append(vocabulary[char])