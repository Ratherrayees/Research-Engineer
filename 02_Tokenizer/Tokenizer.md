# Tokenizer — Curriculum & Progress

## Purpose

This track explains how raw text becomes the token IDs that a language model can process, and how generated token IDs become text again.

The goal is to understand:

* what tokens are,
* how vocabularies work,
* how text is encoded and decoded,
* why simple word tokenization is insufficient,
* why subword tokenization exists,
* how BPE learns reusable pieces,
* how trained merge rules are applied to unseen text,
* how production tokenizers handle bytes, Unicode, whitespace, punctuation, special tokens, padding, truncation, and sequence preparation.

This track should move from simple manual tokenizers to production-grade tokenizer concepts.

---

# Stage 1 — What Is a Token?

## Concepts

* [x] Token
* [x] Tokenizer
* [x] Raw text
* [x] Token sequence
* [x] Token ID
* [x] Vocabulary

## Core Mental Model

A token is a unit produced by a tokenizer.

A token does not necessarily equal a word.

A token may represent:

* a whole word,
* part of a word,
* punctuation,
* whitespace-related text,
* a number fragment,
* a byte-level piece,
* or another reusable text pattern.

The basic pipeline is:

```text
Text
↓
Tokenizer
↓
Tokens
↓
Token IDs
```

---

# Stage 2 — Word-Level Tokenization

## Completed

* [x] Split sentence using whitespace
* [x] Produce word-like tokens
* [x] Preserve punctuation attached to words
* [x] Observe repeated tokens
* [x] Build tokenizer from scratch

## Example Mental Model

```text
"Hello AI"

↓

["Hello", "AI"]
```

In our first tokenizer:

```text
token = whitespace-separated piece
```

This is useful for learning but not sufficient for modern LLMs.

---

# Stage 3 — Vocabulary

## Concepts

* [x] Unique tokens
* [x] Vocabulary dictionary
* [x] Token → ID mapping
* [x] Same token → same ID
* [x] IDs assigned sequentially
* [x] IDs are identifiers, not meaning

## Mental Model

```text
"AI" → 4
"learn" → 17
```

The number itself does not represent semantic meaning.

It identifies the token's position or entry in the tokenizer vocabulary.

---

# Stage 4 — Encoding

## Concepts

* [x] Text → tokens
* [x] Tokens → IDs
* [x] Repeated token IDs
* [x] Encoded token sequence

## Core Flow

```text
Text
↓
Tokens
↓
Vocabulary lookup
↓
Token IDs
```

Encoding is the process of turning text into the numerical identifiers used by the model pipeline.

---

# Stage 5 — Decoding

## Concepts

* [x] Token IDs → tokens
* [x] Reverse lookup
* [x] Reverse vocabulary
* [x] Reconstruct sentence

## Improvement From Day 001 to Day 002

Original vocabulary:

```text
token → ID
```

Reverse vocabulary:

```text
ID → token
```

This made decoding direct rather than searching through the original vocabulary.

---

# Stage 6 — Reverse Vocabulary

## Completed

* [x] Build reverse vocabulary once
* [x] Direct ID lookup
* [x] Decode token IDs
* [x] Join decoded tokens into text

## Core Insight

Encoding and decoding use opposite lookup directions:

```text
Encoding:
token → ID

Decoding:
ID → token
```

---

# Stage 7 — Limitations of Simple Word Tokenization

## Punctuation

Completed observation:

```text
AI
AI,
AI.
```

can become three different tokens.

* [x] Punctuation problem
* [x] Attached punctuation creates separate entries

---

## Case Sensitivity

Potentially:

```text
AI
ai
Ai
```

can become separate vocabulary entries.

* [x] Basic case-sensitivity awareness
* [ ] Explore normalization choices

---

## Unknown Words

Suppose vocabulary contains:

```text
I
love
AI
```

but receives:

```text
transformers
```

A pure whole-word tokenizer may have no ID for it.

* [x] Unknown-word problem
* [x] Understand `<UNK>` conceptually
* [x] Understand information loss from unknown tokens

---

## Vocabulary Explosion

A word-level tokenizer may need separate entries for:

* inflections,

* names,

* punctuation combinations,

* spelling variants,

* scientific terms,

* URLs,

* code,

* numbers,

* new words.

* [x] Understand vocabulary explosion problem

---

# Stage 8 — Character-Level Tokenization

## Concepts

* [x] Character as smallest learning unit
* [x] Character tokenizer intuition
* [x] Unknown-word reduction
* [x] Longer-sequence disadvantage

## Trade-Off

Word level:

```text
"learning" → one token
```

Character level:

```text
"learning" → l e a r n i n g
```

Word-level advantage:

* short sequences

Word-level disadvantage:

* large vocabulary

Character-level advantage:

* small vocabulary

Character-level disadvantage:

* long sequences

This trade-off motivates subword tokenization.

---

# Stage 9 — Subword Tokenization

## Concepts

* [x] Reusable pieces
* [x] Common words may remain whole
* [x] Rare words may split
* [x] Word ≠ token
* [x] Token ≠ word
* [x] Vocabulary-size vs sequence-length trade-off

## Mental Model

Conceptually:

```text
learning → learn + ing
learned  → learn + ed
learner  → learn + er
```

The exact split depends on the tokenizer.

---

# Stage 10 — Why BPE Exists

## BPE

Byte Pair Encoding

For our learning implementation, we begin with characters rather than raw bytes.

The central idea is:

> Frequently occurring neighboring pieces are repeatedly merged into larger reusable tokens.

Core process:

```text
Small units
↓
Count adjacent pairs
↓
Find most frequent pair
↓
Merge it
↓
Repeat
```

* [x] BPE motivation
* [x] BPE intuition
* [x] Frequency-driven merging
* [x] BPE is statistical, not grammatical

---

# Stage 11 — BPE Training Corpus

## Concepts

* [x] Corpus
* [x] Frequency matters
* [x] Repeated patterns are useful
* [x] Tokenizer training data affects learned vocabulary

## Important Insight

BPE does not know that:

```text
learn
```

is a linguistic root.

It only sees repeated token combinations.

If certain sequences occur frequently, they may become reusable tokens.

---

# Stage 12 — Preserve Word Boundaries

## Simplified Learning Implementation

We split:

```text
corpus
↓
words
↓
characters inside each word
```

Instead of flattening the entire corpus into one character stream.

Example:

```text
[
  ['l', 'e', 'a', 'r', 'n'],
  ['l', 'e', 'a', 'r', 'n', 'i', 'n', 'g']
]
```

* [x] Keep each word as a separate inner list
* [x] Prevent accidental cross-word pair counting
* [x] Understand why flattening loses boundaries

---

# Stage 13 — Count Neighboring Pairs

## Completed

* [x] Traverse each word
* [x] Inspect current and next token
* [x] Create pair tuple
* [x] Count pair frequency
* [x] Combine counts across corpus

## Example

For:

```text
['l', 'e', 'a', 'r', 'n']
```

pairs are:

```text
('l','e')
('e','a')
('a','r')
('r','n')
```

The frequency table answers:

> Which neighboring pieces appear together most often?

---

# Stage 14 — Find Most Frequent Pair

## Completed

* [x] Compare pair frequencies
* [x] Select highest-frequency pair
* [x] Understand `max(..., key=...)` concept

## BPE Question

At each round:

> Which pair should become one token next?

---

# Stage 15 — Merge Most Frequent Pair

## Completed

* [x] Scan each word left to right
* [x] Detect matching pair
* [x] Join pair
* [x] Move forward by two positions after merge
* [x] Move forward by one otherwise
* [x] Build a new token list
* [x] Avoid modifying the current list while traversing it

## Example

```text
['l', 'e', 'a', 'r', 'n']
```

with:

```text
('l','e')
```

becomes:

```text
['le', 'a', 'r', 'n']
```

---

# Stage 16 — Repeat BPE Merges

## Completed

* [x] Replace previous token structure
* [x] Recount pairs
* [x] Find next most-common pair
* [x] Repeat
* [x] Add merge-round counter
* [x] Add maximum merge rounds

## Core Loop

```text
Count
↓
Choose
↓
Merge
↓
Recount
↓
Repeat
```

This is the heart of BPE training.

---

# Stage 17 — Observe Larger Pieces Emerging

## Completed

The tokenizer showed progressive constructions such as:

```text
to
↓
tok
↓
token
↓
tokeniz
↓
tokenizer
```

and:

```text
th
↓
the
```

and:

```text
in
↓
ing
```

This demonstrates that BPE gradually builds larger units from smaller ones.

* [x] Observe character pair merging
* [x] Observe subword formation
* [x] Observe full-word formation

---

# Stage 18 — Merge Rules

## Completed

We created a list containing one learned pair per BPE round.

Example:

```text
[
  ('e','n'),
  ('t','h'),
  ('t','o'),
  ('i','n'),
  ...
]
```

* [x] Save most-common pair once per round
* [x] Preserve learned order
* [x] Understand that merge order matters

## Why Merge Order Matters

Suppose rules are:

```text
('t','o') → to
('to','k') → tok
('tok','en') → token
```

`tok` cannot be used before earlier merges create it.

Therefore:

> BPE merge rules form an ordered sequence.

---

# Stage 19 — Tokenizer Training vs Tokenizer Use

## Very Important Distinction

### Training

```text
Corpus
↓
Discover frequent pairs
↓
Learn merge rules
↓
Build vocabulary
```

### Use

```text
New text
↓
Break into initial units
↓
Apply learned merge rules
↓
Produce tokens
↓
Convert to IDs
```

* [x] Understand the distinction conceptually
* [ ] Implement reusable encoding of unseen text

---

# Stage 20 — Build BPE Vocabulary

## Completed

After merge training, unique final token pieces receive IDs.

Example:

```text
th        → 0
in        → 1
ing       → 2
token     → 3
tokenizer → 4
```

* [x] Unique BPE pieces
* [x] Assign integer IDs
* [x] Token → ID vocabulary

---

# Stage 21 — Encode BPE Pieces

## Completed

Final learned token pieces are mapped into IDs.

So the pipeline now reaches:

```text
Corpus
↓
Characters
↓
BPE merges
↓
Subword tokens
↓
Vocabulary
↓
Token IDs
```

* [x] Encode final BPE tokens
* [x] Produce flat token ID sequence

---

# Stage 22 — Apply BPE to Unseen Words

## Current Major Milestone

This is the next step.

## Goal

Give the trained tokenizer a word it did not directly train as one complete token.

Example conceptually:

```text
unseen word
↓
split into characters
↓
apply merge rules in learned order
↓
remaining subword pieces
↓
IDs
```

## Tasks

* [ ] Accept unseen word
* [ ] Convert word to initial character tokens
* [ ] Loop through stored merge rules
* [ ] Apply matching merge rules in order
* [ ] Produce final subword pieces
* [ ] Inspect result
* [ ] Convert pieces to vocabulary IDs

---

# Stage 23 — Apply BPE to Unseen Sentences

## Depends On

* unseen-word tokenization
* word boundaries
* punctuation handling

## Tasks

* [ ] Split new sentence appropriately
* [ ] Tokenize every word
* [ ] Preserve boundaries
* [ ] Produce one token sequence
* [ ] Encode sequence into IDs

---

# Stage 24 — Vocabulary Coverage Problem

## Important Upcoming Issue

A learned merge may produce useful pieces, but an unseen character or token still needs representation.

Topics:

* [ ] Base vocabulary
* [ ] Character coverage
* [ ] Unknown characters
* [ ] Fallback behavior
* [ ] Why byte-level tokenization helps

---

# Stage 25 — Exact Decoding

## Current Limitation

Our simplified tokenizer splits by whitespace but then flattens encoded pieces.

That means spaces are not explicitly encoded.

Exact reconstruction therefore needs better boundary handling.

## Topics

* [ ] Preserve word boundaries
* [ ] Boundary marker
* [ ] Explicit whitespace token
* [ ] Join rules
* [ ] Punctuation reconstruction
* [ ] Decode token IDs exactly

---

# Stage 26 — Whitespace Handling

## Concepts

Real tokenizers often treat whitespace as meaningful.

Potential representations include:

* explicit space tokens,
* leading-space markers,
* byte representations,
* whitespace merged with neighboring text.

## Topics

* [ ] Why spaces matter
* [ ] Leading space vs no leading space
* [ ] Exact-text reconstruction
* [ ] Whitespace tokenization strategies

---

# Stage 27 — Punctuation Handling

## Topics

* [x] Observe punctuation attachment problem
* [ ] Separate punctuation
* [ ] Merge punctuation statistically
* [ ] Punctuation as independent token
* [ ] Punctuation attached to subword token
* [ ] Exact decoding

---

# Stage 28 — Normalization

## Optional but Useful

Some tokenizer pipelines normalize text before tokenization.

Topics:

* [ ] Lowercasing
* [ ] Case preservation
* [ ] Unicode normalization
* [ ] Whitespace normalization
* [ ] Normalization trade-offs

Important:

Normalization may simplify vocabulary but can destroy distinctions.

---

# Stage 29 — Unicode

## Why It Matters

Human text is not limited to ASCII.

We need to eventually understand:

* English letters
* Arabic script
* Devanagari
* Chinese characters
* emoji
* mathematical symbols
* unusual punctuation

## Topics

* [ ] Unicode code points
* [ ] Character vs byte
* [ ] Unicode normalization
* [ ] Multi-byte characters

---

# Stage 30 — UTF-8 and Bytes

## Prerequisites for Byte-Level BPE

* [ ] What is a byte?
* [ ] 8-bit value
* [ ] UTF-8
* [ ] Characters encoded as bytes
* [ ] One character may use multiple bytes

## Goal

Understand why bytes provide a universal low-level representation for text.

---

# Stage 31 — Byte-Level Tokenization

## Why It Exists

A byte-based tokenizer can begin with a finite base vocabulary covering byte values.

This greatly reduces unknown-text problems.

Conceptually:

```text
text
↓
UTF-8 bytes
↓
byte-level units
↓
BPE merges
```

## Topics

* [ ] Byte vocabulary
* [ ] Byte fallback
* [ ] Arbitrary Unicode representation
* [ ] Byte sequences
* [ ] Byte-level BPE

---

# Stage 32 — Byte-Level BPE

## Concepts

* [ ] BPE starting from bytes
* [ ] Merge frequent byte sequences
* [ ] Larger text pieces emerge
* [ ] Near-universal text coverage
* [ ] Trade-offs

## Goal

Connect our simplified character-level BPE with GPT-style tokenizer design.

---

# Stage 33 — Vocabulary Size

## Concepts

* [ ] Small vocabulary
* [ ] Large vocabulary
* [ ] Sequence length
* [ ] Embedding-table size
* [ ] Training frequency
* [ ] Rare tokens
* [ ] Context efficiency

## Trade-Off

Small vocabulary:

```text
fewer vocabulary entries
but
more tokens per text
```

Large vocabulary:

```text
more vocabulary entries
but
potentially shorter token sequences
```

---

# Stage 34 — Tokenizer Training Corpus

## Topics

* [ ] Corpus diversity
* [ ] Languages
* [ ] Code
* [ ] Numbers
* [ ] Scientific text
* [ ] Web text
* [ ] Frequency imbalance
* [ ] Domain bias

## Important Insight

Tokenizer design can favor text patterns common in its training corpus.

Therefore tokenizer efficiency may vary across:

* languages,
* domains,
* programming languages,
* technical terminology.

---

# Stage 35 — Token Frequency

## Topics

* [ ] Frequent pieces
* [ ] Rare pieces
* [ ] Merge frequency
* [ ] Vocabulary allocation
* [ ] Frequency thresholds

## Connection

BPE is fundamentally driven by frequency.

---

# Stage 36 — Special Tokens

## Why They Exist

Some tokens are not ordinary text fragments.

They represent model-control concepts.

## Topics

* [ ] BOS — beginning of sequence
* [ ] EOS — end of sequence
* [ ] PAD — padding
* [ ] UNK — unknown token
* [ ] MASK — masked token
* [ ] Separator tokens
* [ ] Chat/control tokens
* [ ] Special-token IDs

---

# Stage 37 — BOS and EOS

## BOS

Beginning Of Sequence

May tell a model:

> a new sequence begins here.

## EOS

End Of Sequence

May signal:

> generation or sequence should end.

Topics:

* [ ] BOS purpose
* [ ] EOS purpose
* [ ] Generation stopping
* [ ] Sequence boundaries

---

# Stage 38 — Padding

## Problem

Sequences have different lengths.

Example:

```text
sequence A → 5 tokens
sequence B → 9 tokens
sequence C → 3 tokens
```

Batched tensor operations usually require consistent dimensions.

Padding adds special tokens so sequences align.

## Topics

* [ ] PAD token
* [ ] Batch shape
* [ ] Left padding
* [ ] Right padding
* [ ] Padding trade-offs

---

# Stage 39 — Attention Masks

## Depends On

* padding
* tensor shapes
* attention

## Concept

The model should usually ignore padding positions.

An attention mask indicates:

```text
real token → attend
padding → ignore
```

Topics:

* [ ] Binary masks
* [ ] Padding masks
* [ ] Mask shape
* [ ] Transformer input masks

---

# Stage 40 — Truncation

## Problem

Input may exceed the model's supported sequence length.

Topics:

* [ ] Maximum length
* [ ] Left truncation
* [ ] Right truncation
* [ ] Information loss
* [ ] Context-window limits

---

# Stage 41 — Context Window Connection

## Important

A context window measured in tokens does not mean words.

Example:

```text
128,000 tokens
```

means tokenizer tokens.

One word may consume:

* 1 token,
* 2 tokens,
* several tokens,
* or more.

## Topics

* [ ] Token density
* [ ] Context efficiency
* [ ] Language differences
* [ ] Code tokenization
* [ ] Long prompts

---

# Stage 42 — Tokenization and Cost

## Practical AI Engineering Connection

Many model APIs measure usage in tokens.

Conceptually:

```text
more tokens
→
more model computation
→
generally more cost
```

Topics:

* [ ] Input tokens
* [ ] Output tokens
* [ ] Token counting
* [ ] Prompt efficiency

---

# Stage 43 — Numbers

## Important Edge Case

Numbers may tokenize in surprising ways.

Examples:

```text
2026
123456
3.14159
```

may split differently depending on tokenizer.

Topics:

* [ ] Digit-level splits
* [ ] Multi-digit tokens
* [ ] Decimal punctuation
* [ ] Numerical reasoning implications

---

# Stage 44 — Code Tokenization

## Topics

* [ ] Indentation
* [ ] Whitespace
* [ ] Symbols
* [ ] Identifiers
* [ ] Repeated programming patterns
* [ ] Programming-language efficiency

## Why It Matters

A tokenizer trained heavily on code may learn tokens for frequent code patterns.

---

# Stage 45 — Multilingual Tokenization

## Topics

* [ ] Different scripts
* [ ] Token density across languages
* [ ] Byte representation
* [ ] Vocabulary allocation
* [ ] Multilingual fairness
* [ ] Efficiency differences

---

# Stage 46 — BPE vs WordPiece vs Unigram

## BPE

* [x] Basic intuition
* [ ] Production-level understanding

Broad idea:

```text
merge frequent neighboring units
```

## WordPiece

* [ ] Basic intuition
* [ ] Vocabulary scoring
* [ ] Subword construction

## Unigram

* [ ] Basic intuition
* [ ] Start with many candidate pieces
* [ ] Remove less useful pieces
* [ ] Probabilistic segmentation

## Goal

Understand that subword tokenization is a family of approaches, not just BPE.

---

# Stage 47 — Tokenizer Training vs Model Training

## Critical Distinction

Tokenizer training decides:

* tokens,
* merge rules,
* vocabulary,
* IDs.

Model training decides:

* embeddings,
* neural-network weights,
* attention behavior,
* language patterns.

## Pipeline

```text
Tokenizer training
↓
Fixed tokenizer
↓
Model training
```

* [x] Understand conceptually
* [ ] Observe with a real tokenizer/model pipeline

---

# Stage 48 — Token IDs vs Embeddings

## Critical Distinction

Token:

```text
"AI"
```

Token ID:

```text
1512
```

Embedding:

```text
[0.31, -0.76, 1.22, ...]
```

## Mental Model

```text
Text
↓
Token
↓
Token ID
↓
Embedding lookup
↓
Vector
```

* [x] Understand basic distinction
* [ ] Implement embedding lookup later

---

# Stage 49 — Production Tokenizer Libraries

After manual understanding:

* [ ] Hugging Face Tokenizers
* [ ] Load pretrained tokenizer
* [ ] Encode text
* [ ] Decode IDs
* [ ] Inspect tokens
* [ ] Inspect vocabulary
* [ ] Inspect special tokens
* [ ] Inspect attention mask
* [ ] Inspect padding
* [ ] Inspect truncation

---

# Stage 50 — Inspect a Real LLM Tokenizer

## Exercise

Take several kinds of text:

* [ ] ordinary English
* [ ] uncommon technical term
* [ ] name
* [ ] number
* [ ] punctuation-heavy text
* [ ] source code
* [ ] non-English language
* [ ] emoji

For each:

* [ ] inspect tokens
* [ ] inspect token IDs
* [ ] count tokens
* [ ] decode back
* [ ] compare behavior

---

# Stage 51 — Tokenizer Evaluation

## Questions

* [ ] How many tokens does common text require?
* [ ] How many tokens do rare words require?
* [ ] How well does tokenizer handle different languages?
* [ ] Can arbitrary text be represented?
* [ ] Can exact text be reconstructed?
* [ ] How large is the vocabulary?
* [ ] How efficient is the context usage?

---

# Optional Advanced Topics

These should not block progress.

## Tokenization Algorithms

* [ ] SentencePiece
* [ ] Unigram Language Model
* [ ] WordPiece details
* [ ] Merge ranking
* [ ] Vocabulary pruning

## Text Normalization

* [ ] NFC
* [ ] NFD
* [ ] NFKC
* [ ] NFKD

## Security / Reliability

* [ ] Invisible Unicode characters
* [ ] Tokenization surprises
* [ ] Prompt boundary issues
* [ ] Adversarial Unicode
* [ ] Token-level prompt injection considerations

## Compression View

* [ ] BPE as compression intuition
* [ ] Repeated pattern replacement
* [ ] Vocabulary efficiency

---

# Practical Exercises

## Exercise 001 — Basic Word Tokenizer

Completed:

* [x] Split sentence
* [x] Vocabulary
* [x] IDs
* [x] Encode
* [x] Decode

---

# Exercise 002 — Improved Word Tokenizer

Completed:

* [x] Reverse vocabulary
* [x] Direct decoding
* [x] Sentence reconstruction
* [x] Observe punctuation limitation

---

# Exercise 003 — BPE Tokenizer Trainer

Completed:

* [x] Corpus
* [x] Split words
* [x] Split characters
* [x] Count pairs
* [x] Find most-common pair
* [x] Merge pair everywhere
* [x] Repeat merges
* [x] Maximum merge rounds
* [x] Save merge rules
* [x] Build final vocabulary
* [x] Encode resulting pieces

---

# Exercise 004 — Reusable BPE Encoder

Next.

Build:

* [ ] new input word
* [ ] initial character tokens
* [ ] apply stored merge rules
* [ ] output subword tokens
* [ ] convert to IDs

---

# Exercise 005 — BPE Sentence Encoder/Decoder

Build:

* [ ] sentence input
* [ ] word boundaries
* [ ] whitespace representation
* [ ] encode
* [ ] decode
* [ ] exact reconstruction

---

# Exercise 006 — Byte-Level Tokenizer

Build simplified:

* [ ] string → UTF-8 bytes
* [ ] bytes → IDs
* [ ] IDs → bytes
* [ ] bytes → original text

Then:

* [ ] apply BPE-style merging

---

# Exercise 007 — Real Tokenizer Inspection

Using a tokenizer library:

* [ ] load tokenizer
* [ ] inspect tokens
* [ ] inspect IDs
* [ ] inspect special tokens
* [ ] compare with our tokenizer

---

# Current Position

Completed:

```text
Text
↓
Word tokens
↓
Vocabulary
↓
Token IDs
↓
Decoding
↓
Reverse vocabulary
↓
Subword motivation
↓
BPE training
↓
Pair counting
↓
Repeated merging
↓
Merge rules
↓
BPE vocabulary
↓
Token IDs
```

Current transition:

```text
Trained BPE
↓
New unseen text
↓
Apply saved merge rules
↓
Reusable tokenizer
```

---

# Immediate Next Topics

Priority:

1. [ ] Apply BPE merge rules to unseen word
2. [ ] Apply BPE to unseen sentence
3. [ ] Preserve word boundaries
4. [ ] Decode BPE IDs
5. [ ] Understand bytes and UTF-8
6. [ ] Byte-level BPE
7. [ ] Special tokens
8. [ ] Padding / truncation
9. [ ] Attention masks
10. [ ] Inspect a production tokenizer

---

# Completion Goal

This track reaches foundation-level completion when the following is fully understandable:

> A tokenizer converts arbitrary text into a finite sequence of token IDs. Modern tokenizers usually represent text using reusable subword or byte-based pieces rather than requiring one vocabulary entry for every possible word. A tokenizer is trained separately from the neural network, and its vocabulary and segmentation choices directly affect sequence length, context efficiency, multilingual behavior, and the model's input representation.

At that point, the next major bridge is:

```text
Token IDs
↓
Embeddings
↓
Neural Network
```
