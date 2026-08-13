# Tensors & Data — Curriculum & Progress

## Purpose

This track explains how data is represented, organized, transformed, and moved through AI systems.

The goal is to understand:

* how numbers become arrays,
* how arrays become vectors, matrices, and tensors,
* how tensor shapes describe data structure,
* how operations work across dimensions,
* how datasets are organized,
* how batching works,
* how sequence data is represented,
* how NumPy and later PyTorch handle this efficiently,
* and how tensor shapes flow through neural networks and transformers.

This track should run in parallel with Math for AI and Model Learning.

---

# Stage 1 — Python Lists vs Numerical Arrays

## Already Encountered

* [x] Python lists
* [x] NumPy installation
* [x] NumPy import
* [x] `np.array`
* [x] `np.mean`

## Topics

* [ ] Python list
* [ ] NumPy array
* [ ] Why arrays exist
* [ ] Homogeneous numerical data
* [ ] Efficient numerical operations
* [ ] Vectorized computation
* [ ] Memory-layout intuition

## Core Difference

Python list:

```text id="lr8tz4"
[1, 2, 3]
```

NumPy array:

```text id="kccmiv"
array([1, 2, 3])
```

They may look similar, but they are built for different purposes.

A NumPy array is designed for efficient numerical computation.

---

# Stage 2 — Why Vectorization Matters

## Concepts

* [x] Multiple values processed together
* [x] Element-wise multiplication
* [x] Element-wise subtraction
* [x] Element-wise squaring
* [ ] Vectorization
* [ ] Python loop vs array operation
* [ ] Why numerical libraries are faster

## Example

Instead of conceptually doing:

```text id="rgy4pl"
prediction1 = x1 * w
prediction2 = x2 * w
prediction3 = x3 * w
```

an array allows:

```text id="jqkc2x"
predictions = x * w
```

where `x` contains many values.

---

# Stage 3 — Scalar

## Topics

* [ ] What is a scalar?
* [ ] Single numerical value
* [ ] Scalar shape intuition
* [ ] Scalar in mathematics
* [ ] Scalar in NumPy
* [ ] Scalar model parameter
* [ ] Scalar loss

## Examples

```text id="2m3hvs"
5
0.01
-3.2
```

Examples in AI:

```text id="11o7ou"
learning rate
single loss value
single weight
temperature
```

---

# Stage 4 — Vector

## Topics

* [ ] What is a vector?
* [ ] Ordered list of numbers
* [ ] One-dimensional array
* [ ] Vector length
* [ ] Vector components
* [ ] Vector shape
* [ ] Input vector
* [ ] Weight vector
* [ ] Embedding vector

## Example

```text id="s12v20"
[2.1, -0.4, 7.3]
```

Potential meaning:

```text id="cd1tpu"
[x1, x2, x3]
```

or:

```text id="36z805"
[w1, w2, w3]
```

or later:

```text id="q4ag32"
embedding vector
```

---

# Stage 5 — Matrix

## Topics

* [ ] What is a matrix?
* [ ] Two-dimensional numerical structure
* [ ] Rows
* [ ] Columns
* [ ] Matrix shape
* [ ] Matrix indexing
* [ ] Matrix as collection of vectors
* [ ] Feature matrix
* [ ] Weight matrix
* [ ] Embedding matrix

## Example

```text id="ql5t13"
[
  [1, 2, 3],
  [4, 5, 6]
]
```

Shape:

```text id="54aut8"
(2, 3)
```

meaning:

```text id="eb8wwi"
2 rows
3 columns
```

---

# Stage 6 — Tensor

## Core Concept

A tensor is a multidimensional numerical array.

## Topics

* [ ] Tensor definition
* [ ] Scalar as 0D tensor
* [ ] Vector as 1D tensor
* [ ] Matrix as 2D tensor
* [ ] 3D tensor
* [ ] Higher-dimensional tensor
* [ ] Tensor vs NumPy array
* [ ] Tensor vs mathematical tensor terminology

## Mental Model

```text id="6r7e1s"
0D → scalar
1D → vector
2D → matrix
3D+ → higher-dimensional tensor
```

In AI engineering, "tensor" often means:

> multidimensional numerical container used for model computation.

---

# Stage 7 — Dimensions

## Topics

* [ ] Number of dimensions
* [ ] Dimension vs size
* [ ] 1D
* [ ] 2D
* [ ] 3D
* [ ] Higher dimensions
* [ ] `ndim`

## Important Distinction

A vector like:

```text id="pybzbp"
[1, 2, 3, 4]
```

has:

```text id="2mjdb8"
1 dimension
```

but contains:

```text id="ond3e5"
4 elements
```

Dimension does not mean number of values.

---

# Stage 8 — Shape

## Critical Topic

## Topics

* [ ] What is shape?
* [ ] Shape tuple
* [ ] Size of each dimension
* [ ] `.shape`
* [ ] Shape reasoning
* [ ] Shape mismatch

## Example

```text id="x9vdjf"
[
  [1, 2, 3],
  [4, 5, 6]
]
```

has shape:

```text id="1ecy21"
(2, 3)
```

Shape tells us how the data is structured.

---

# Stage 9 — Axis

## Topics

* [ ] What is an axis?
* [ ] Axis 0
* [ ] Axis 1
* [ ] Higher axes
* [ ] Reducing along an axis
* [ ] Summing across an axis
* [ ] Taking mean across an axis

## Example Mental Model

For a matrix:

```text id="e4q13m"
rows × columns
```

different axes allow us to ask:

> Should this operation combine values across rows or columns?

This becomes extremely important in:

* mean calculations,
* softmax,
* normalization,
* attention.

---

# Stage 10 — Size

## Topics

* [ ] Total number of elements
* [ ] Shape vs size
* [ ] `.size`
* [ ] Product of dimensions

Example:

```text id="ea6p8b"
shape = (2, 3)
```

contains:

```text id="de702q"
2 × 3 = 6 elements
```

---

# Stage 11 — Data Types

## Topics

* [ ] `dtype`
* [ ] Integer
* [ ] Floating point
* [ ] Boolean
* [ ] String/object limitations
* [ ] `int32`
* [ ] `int64`
* [ ] `float32`
* [ ] `float64`

## AI Connection

Model parameters usually use floating-point values.

Token IDs generally use integer types.

Attention masks may use integers, booleans, or floats depending on implementation.

---

# Stage 12 — Indexing

## Topics

* [ ] Select one element
* [ ] Positive index
* [ ] Negative index
* [ ] Index vectors
* [ ] Index matrices
* [ ] Row indexing
* [ ] Column indexing
* [ ] Multi-dimensional indexing

## Goal

Be comfortable answering:

> Where exactly is this number inside the tensor?

---

# Stage 13 — Slicing

## Topics

* [ ] Start index
* [ ] Stop index
* [ ] Step
* [ ] Slice vector
* [ ] Slice rows
* [ ] Slice columns
* [ ] Slice higher-dimensional arrays

## AI Connection

Used frequently for:

* selecting batches,
* selecting sequence ranges,
* shifting language-model targets,
* selecting attention heads.

---

# Stage 14 — Element-Wise Operations

## Already Encountered

* [x] Multiplication
* [x] Subtraction
* [x] Squaring

## Additional Topics

* [ ] Addition
* [ ] Division
* [ ] Comparison
* [ ] Powers
* [ ] Element-wise functions
* [ ] Shape requirements

## Important

Element-wise multiplication:

```text id="03d4wm"
A * B
```

is not the same as matrix multiplication.

This distinction becomes critical later.

---

# Stage 15 — Reduction Operations

## Topics

* [x] Mean
* [ ] Sum
* [ ] Minimum
* [ ] Maximum
* [ ] Product
* [ ] Reduce entire tensor
* [ ] Reduce selected axis
* [ ] Keep dimensions

## AI Connection

Used for:

* batch loss
* average metrics
* normalization
* attention operations
* statistics

---

# Stage 16 — Broadcasting

## Critical NumPy/PyTorch Concept

Broadcasting allows tensors with compatible shapes to interact even if their shapes are not identical.

## Topics

* [ ] Scalar + vector
* [ ] Vector + matrix
* [ ] Broadcasting rules
* [ ] Trailing dimensions
* [ ] Dimension compatibility
* [ ] Shape expansion intuition
* [ ] Broadcasting errors

## Neural Network Connection

Bias addition frequently relies on broadcasting.

Conceptually:

```text id="2v0tbo"
matrix output
+
bias vector
```

without manually copying the bias for every sample.

---

# Stage 17 — Reshape

## Topics

* [ ] Change tensor shape
* [ ] Preserve number of elements
* [ ] `.reshape`
* [ ] Shape compatibility
* [ ] Automatic dimension inference
* [ ] Why reshaping is useful

## Important Rule

Reshaping changes the structure used to view the data.

It does not normally change the values themselves.

---

# Stage 18 — Flatten

## Topics

* [ ] Convert multiple dimensions into one
* [ ] Flatten matrices
* [ ] Flatten tensors
* [ ] Information about shape can be lost

## AI Connection

Useful in some neural-network architectures and data preparation.

---

# Stage 19 — Transpose

## Topics

* [ ] Swap dimensions
* [ ] Matrix transpose
* [ ] Rows become columns
* [ ] NumPy transpose
* [ ] Shape changes

## Transformer Connection

Later we will encounter operations involving:

```text id="b8oy31"
Q × Kᵀ
```

Transpose must feel natural before reaching attention.

---

# Stage 20 — Concatenation

## Topics

* [ ] Combine arrays along existing axis
* [ ] Concatenate vectors
* [ ] Concatenate matrices
* [ ] Axis choice
* [ ] Shape requirements

## Transformer Connection

Multi-head attention eventually concatenates outputs from separate heads.

---

# Stage 21 — Stacking

## Topics

* [ ] Create a new dimension
* [ ] Stack vectors
* [ ] Stack matrices
* [ ] Stack vs concatenate

## Example Concept

Several samples can be stacked into one batch.

---

# Stage 22 — Dot Product

## Cross-Track Topic

This belongs mathematically to Math for AI but computationally appears here.

## Topics

* [ ] Manual dot product
* [ ] NumPy dot product
* [ ] Shape requirements
* [ ] Scalar output
* [ ] Weighted-sum interpretation

## Neural Network Connection

```text id="74gowu"
input vector · weight vector
```

is the mathematical core of one neuron.

---

# Stage 23 — Matrix-Vector Multiplication

## Topics

* [ ] Matrix × vector
* [ ] Multiple dot products
* [ ] Output vector
* [ ] Shape reasoning
* [ ] NumPy implementation

## Neural Network Connection

Multiple neurons can be represented by one weight matrix.

---

# Stage 24 — Matrix Multiplication

## Critical Topic

## Topics

* [ ] Matrix × matrix
* [ ] Inner dimension requirement
* [ ] Output shape
* [ ] `@`
* [ ] `np.matmul`
* [ ] Element-wise vs matrix multiplication

## Example Shape Reasoning

```text id="9sub50"
(A, B) @ (B, C)
→
(A, C)
```

This pattern appears everywhere in modern AI.

---

# Stage 25 — Batch Matrix Multiplication

## Later Topic

## Topics

* [ ] Multiple matrices processed together
* [ ] Batch dimension
* [ ] Batched matrix multiply
* [ ] Higher-dimensional shape rules

## Transformer Connection

Attention calculations happen across:

* batches,
* heads,
* sequences.

---

# Stage 26 — Dataset

## Concepts

* [ ] What is a dataset?
* [ ] Observation/sample
* [ ] Input
* [ ] Target
* [ ] Features
* [ ] Labels
* [ ] Dataset size

## Example

A simple regression dataset:

```text id="ur1r9y"
x → input
y → target
```

with multiple rows representing separate training examples.

---

# Stage 27 — Sample

## Topics

* [ ] One observation
* [ ] One input
* [ ] One target
* [ ] Feature vector
* [ ] Sample shape

Example:

```text id="f6opja"
sample = [height, weight, age]
```

could represent three features for one observation.

---

# Stage 28 — Feature

## Topics

* [ ] Input property
* [ ] Single feature
* [ ] Multiple features
* [ ] Feature vector
* [ ] Feature dimension

## Connection to Multiple Weights

If one sample has:

```text id="o6fwn0"
3 features
```

a simple neuron may have:

```text id="ij7sma"
3 corresponding weights
```

---

# Stage 29 — Target / Label

## Topics

* [ ] Regression target
* [ ] Classification label
* [ ] Language-model target token
* [ ] Input vs target separation

## Language Model Connection

Later:

```text id="cafmri"
input tokens
↓
predict next token
↓
actual next token = target
```

---

# Stage 30 — Feature Matrix

## Topics

* [ ] Samples as rows
* [ ] Features as columns
* [ ] Dataset matrix
* [ ] Shape

Example:

```text id="knc4me"
[num_samples, num_features]
```

This is a major bridge into neural-network input representation.

---

# Stage 31 — Target Vector

## Topics

* [ ] One target per sample
* [ ] Vector of targets
* [ ] Regression targets
* [ ] Classification labels

Example:

```text id="5s0o9s"
[num_samples]
```

or sometimes:

```text id="vv9umw"
[num_samples, output_features]
```

---

# Stage 32 — Batch

## Critical AI Concept

A batch is a group of samples processed together.

## Topics

* [ ] Batch
* [ ] Batch size
* [ ] Why batches are useful
* [ ] Batch tensor
* [ ] One batch vs full dataset

## Example

Dataset:

```text id="h5yzab"
10,000 samples
```

Batch size:

```text id="ykzu92"
32
```

Training processes subsets of 32 samples at a time.

---

# Stage 33 — Batch Dimension

## Topics

* [ ] First dimension often represents batch
* [ ] Single sample shape
* [ ] Batched sample shape
* [ ] Dynamic batch sizes

Example:

Single vector:

```text id="5g8huj"
[features]
```

Batch:

```text id="f8nxx7"
[batch, features]
```

---

# Stage 34 — Epoch

## Topics

* [ ] Epoch
* [ ] Entire dataset processed once
* [ ] Multiple batches per epoch
* [ ] Multiple epochs

## Conceptual Flow

```text id="7rc0d6"
Dataset
↓
Batch 1
Batch 2
Batch 3
...
↓
one epoch complete
```

---

# Stage 35 — Step / Iteration

## Topics

* [ ] One optimizer update
* [ ] One batch processed
* [ ] Step vs epoch
* [ ] Number of steps per epoch

Later:

```text id="7mf0jm"
forward
↓
loss
↓
backward
↓
optimizer update
```

typically represents one training step.

---

# Stage 36 — Shuffling

## Topics

* [ ] Randomize sample order
* [ ] Why order can matter
* [ ] Shuffle before epochs
* [ ] Reproducibility
* [ ] Random seed

## Goal

Prevent undesirable learning patterns caused by fixed data ordering.

---

# Stage 37 — Training Set

## Topics

* [ ] Data used to update parameters
* [ ] Training loss
* [ ] Model learns from these examples

---

# Stage 38 — Validation Set

## Topics

* [ ] Data not used for gradient updates
* [ ] Validation loss
* [ ] Hyperparameter decisions
* [ ] Detect overfitting

---

# Stage 39 — Test Set

## Topics

* [ ] Final evaluation data
* [ ] Held-out data
* [ ] Avoid repeated tuning against test results

---

# Stage 40 — Dataset Splitting

## Topics

* [ ] Train / validation / test
* [ ] Split ratios
* [ ] Random splitting
* [ ] Stratified splitting concept
* [ ] Time-based splitting concept

## Important

The correct split strategy depends on the data.

---

# Stage 41 — Data Leakage

## Critical Engineering Topic

## Topics

* [ ] Train/test contamination
* [ ] Future information leaking into training
* [ ] Duplicate examples
* [ ] Preprocessing leakage
* [ ] Leakage causing misleading evaluation

## Goal

Understand:

> A model can appear good because the evaluation setup is flawed.

---

# Stage 42 — Data Shuffling vs Sequence Order

## Important Distinction

For independent samples:

```text id="zqblbe"
shuffling is often useful
```

For sequence/time data:

```text id="u6qbbp"
order may contain essential information
```

This becomes important for:

* time series,
* language sequences,
* autoregressive models.

---

# Stage 43 — Data Normalization

## Topics

* [ ] Scaling values
* [ ] Why feature magnitude matters
* [ ] Min-max scaling intuition
* [ ] Standardization
* [ ] Mean subtraction
* [ ] Divide by standard deviation

## Neural Network Connection

Well-scaled inputs can make optimization easier.

---

# Stage 44 — Standardization

## Topics

* [ ] Mean
* [ ] Standard deviation
* [ ] Center around zero
* [ ] Unit-scale intuition
* [ ] Fit statistics using training data only

## Data Leakage Connection

Validation/test data should not be used to calculate training normalization statistics.

---

# Stage 45 — Missing Data

## Topics

* [ ] Missing values
* [ ] Detect missing values
* [ ] Remove rows
* [ ] Imputation
* [ ] Missingness itself may contain information

Optional until working with real tabular datasets.

---

# Stage 46 — Categorical Data

## Topics

* [ ] Categories
* [ ] Integer encoding
* [ ] One-hot encoding
* [ ] Embedding categorical values
* [ ] Ordinal vs nominal data

Optional for language-model path but valuable for general ML engineering.

---

# Stage 47 — Sequence Data

## Critical for LLMs

A sentence becomes an ordered token sequence.

Conceptually:

```text id="5kmf59"
[token1, token2, token3, token4]
```

## Topics

* [ ] Sequence
* [ ] Sequence length
* [ ] Position
* [ ] Variable-length sequences
* [ ] Token ID sequence

---

# Stage 48 — Token ID Tensor

## Tokenizer Connection

Tokenizer output:

```text id="240l8d"
[12, 85, 291, 7]
```

can be stored as a tensor.

## Topics

* [ ] Integer token IDs
* [ ] One sequence
* [ ] Batch of token sequences
* [ ] Integer dtype

---

# Stage 49 — Sequence Length

## Topics

* [ ] Number of tokens
* [ ] Maximum sequence length
* [ ] Short sequences
* [ ] Long sequences
* [ ] Context length

## Important

Sequence length measures:

```text id="w3qxsg"
tokens
```

not necessarily words.

---

# Stage 50 — Variable-Length Sequences

## Problem

Sentences naturally have different token counts.

Example:

```text id="zfq98t"
sentence A → 4 tokens
sentence B → 10 tokens
sentence C → 7 tokens
```

But batched tensors usually require aligned shapes.

Unlocks:

* padding
* attention masks

---

# Stage 51 — Padding

## Tokenizer/Data Connection

## Topics

* [ ] Pad shorter sequences
* [ ] Padding token
* [ ] Same batch length
* [ ] Left padding
* [ ] Right padding

Example:

```text id="rr0p8q"
[12, 7, 9, PAD, PAD]
[31, 5, 8, 17, 22]
```

Now both rows have the same length.

---

# Stage 52 — Attention Mask

## Later Transformer Connection

Padding is not real content.

The model therefore needs information about which positions should be ignored.

Example concept:

```text id="p4tjwx"
tokens:
[A, B, C, PAD, PAD]

mask:
[1, 1, 1, 0, 0]
```

## Topics

* [ ] Mask tensor
* [ ] Real positions
* [ ] Padding positions
* [ ] Shape of attention masks

---

# Stage 53 — Basic Language Batch Shape

Before embeddings:

```text id="9hts2n"
[batch, sequence]
```

Example:

```text id="3n9m04"
[32, 128]
```

means:

```text id="u9gdsc"
32 sequences
128 token positions per sequence
```

---

# Stage 54 — Embedding Shape

After token IDs are converted into embeddings:

```text id="st6wqa"
[batch, sequence]
```

becomes:

```text id="pgz57i"
[batch, sequence, embedding]
```

Example:

```text id="53qjwo"
[32, 128, 768]
```

means:

```text id="prkz6h"
32 sequences
128 token positions each
768 numbers representing each token
```

This is one of the most important shapes in transformer engineering.

---

# Stage 55 — Embedding Table Shape

Later:

```text id="5otn2g"
[vocabulary_size, embedding_dimension]
```

Example:

```text id="umv0yd"
[50,000, 768]
```

Each vocabulary entry corresponds to one row.

Token ID:

```text id="ro897p"
42
```

selects:

```text id="6jdr5v"
row 42
```

producing one embedding vector.

---

# Stage 56 — Hidden State Tensor

Inside a transformer:

```text id="bkmxax"
[batch, sequence, hidden_dimension]
```

The model repeatedly transforms this tensor while preserving or modifying its representation.

## Topics

* [ ] Hidden state
* [ ] Hidden dimension
* [ ] Representation at each token position

---

# Stage 57 — Vocabulary Logits Shape

At language-model output:

```text id="i2yzy3"
[batch, sequence, vocabulary]
```

Example:

```text id="tmxyy6"
[32, 128, 50,000]
```

This means that for every:

* sequence,
* token position,

the model produces a score for every possible next token.

---

# Stage 58 — Shape Tracking

## Critical Engineering Skill

At every step ask:

```text id="dy8a59"
What is the input shape?
What operation happens?
What is the output shape?
```

## Example Pipeline

```text id="t0nnz8"
Token IDs
[batch, sequence]

↓

Embeddings
[batch, sequence, hidden]

↓

Transformer blocks
[batch, sequence, hidden]

↓

Vocabulary projection
[batch, sequence, vocabulary]
```

Shape tracking should become automatic.

---

# Stage 59 — Reshaping for Multi-Head Attention

## Later Topic

Suppose hidden dimension is divided across attention heads.

Conceptually:

```text id="12h8fo"
[batch, sequence, hidden]
```

may be reorganized into:

```text id="c70jfp"
[batch, heads, sequence, head_dimension]
```

## Topics

* [ ] Split dimension
* [ ] Rearrange axes
* [ ] Preserve total number of values
* [ ] Merge heads later

This is one reason strong tensor-shape understanding is essential before attention.

---

# Stage 60 — Permute / Axis Reordering

## Later PyTorch Topic

## Topics

* [ ] Reorder axes
* [ ] Difference from reshape
* [ ] Sequence/head dimension swaps
* [ ] Attention calculation shapes

---

# Stage 61 — Contiguous Memory Intuition

## Optional Engineering Topic

Some tensor operations alter how a tensor views underlying memory.

Topics:

* [ ] Logical shape vs memory layout
* [ ] Contiguous data
* [ ] Views
* [ ] Copies

Useful later when debugging PyTorch performance and reshape behavior.

---

# Stage 62 — Copies vs Views

## Optional but Valuable

## Topics

* [ ] Copy data
* [ ] View same data differently
* [ ] Mutation effects
* [ ] Memory implications

This becomes useful in numerical Python and PyTorch.

---

# Stage 63 — Random Arrays

## Topics

* [ ] Random numbers
* [ ] Uniform random values
* [ ] Normal random values
* [ ] Random initialization
* [ ] Random seed

## Neural Network Connection

Model weights are commonly initialized using random values following carefully chosen distributions.

---

# Stage 64 — Reproducibility

## Topics

* [ ] Random seed
* [ ] Deterministic experiments
* [ ] NumPy seed
* [ ] PyTorch seed later
* [ ] Why exact reproduction can still be difficult

## AI Engineering Connection

Experiments should be reproducible enough to compare changes reliably.

---

# Stage 65 — Data Distribution

## Topics

* [ ] Distribution of values
* [ ] Mean
* [ ] Variance
* [ ] Outliers
* [ ] Class imbalance
* [ ] Long tails

## Goal

Understand that the numerical structure of data affects model learning.

---

# Stage 66 — Sampling

## Topics

* [ ] Sample subset
* [ ] Random sampling
* [ ] Biased sampling
* [ ] Representative samples
* [ ] Sampling without replacement
* [ ] Sampling with replacement

---

# Stage 67 — Class Imbalance

## General ML Topic

## Topics

* [ ] Majority class
* [ ] Minority class
* [ ] Misleading accuracy
* [ ] Weighted loss concept
* [ ] Resampling concept

Optional until classification projects begin.

---

# Stage 68 — Dataset Bias

## Important AI Engineering Topic

## Topics

* [ ] Sampling bias
* [ ] Representation imbalance
* [ ] Historical bias
* [ ] Domain imbalance
* [ ] Measurement bias

## Goal

Understand:

> A model can only learn from the data and objective it receives.

Poor or skewed data can produce poor or skewed behavior.

---

# Stage 69 — Data Quality

## Topics

* [ ] Incorrect labels
* [ ] Duplicate data
* [ ] Corrupted examples
* [ ] Outliers
* [ ] Noise
* [ ] Formatting inconsistencies

## LLM Connection

Large language-model performance depends heavily on corpus quality, not just corpus size.

---

# Stage 70 — Deduplication

## Later LLM Data Topic

## Topics

* [ ] Exact duplicates
* [ ] Near duplicates
* [ ] Why duplicates matter
* [ ] Memorization
* [ ] Evaluation contamination

---

# Stage 71 — Data Pipeline

## Goal

Understand the complete flow:

```text id="lgwjmf"
Raw data
↓
Cleaning
↓
Transformation
↓
Tokenization / numerical encoding
↓
Dataset
↓
Batches
↓
Model
```

## Topics

* [ ] Input pipeline
* [ ] Transformation stages
* [ ] Batch generation
* [ ] Model-ready tensors

---

# Stage 72 — Dataset → DataLoader

## Later PyTorch Connection

Conceptually:

```text id="49papj"
Dataset
↓
DataLoader
↓
Batch
↓
Model
```

Topics:

* [ ] Dataset object
* [ ] DataLoader
* [ ] Batch size
* [ ] Shuffle
* [ ] Collation
* [ ] Workers

---

# Stage 73 — Collation

## Sequence Data Topic

A collate operation combines separate samples into a batch.

For text, this may involve:

* tokenization,
* padding,
* masks,
* stacking.

## Topics

* [ ] Sample list
* [ ] Batch construction
* [ ] Custom collate functions
* [ ] Dynamic padding

---

# Stage 74 — Static vs Dynamic Padding

## Topics

* [ ] Pad everything to global maximum
* [ ] Pad only to longest sequence in current batch
* [ ] Memory efficiency
* [ ] Computational efficiency

Useful later in language-model training.

---

# Stage 75 — Bucketing by Sequence Length

## Optional Optimization

Grouping similarly sized sequences can reduce wasted padding.

Topics:

* [ ] Length buckets
* [ ] Padding waste
* [ ] Throughput improvements

---

# Stage 76 — Memory Usage

## Important Engineering Topic

Tensor storage roughly depends on:

```text id="ddmz6t"
number of elements
×
bytes per element
```

## Topics

* [ ] Element count
* [ ] dtype size
* [ ] Tensor memory
* [ ] Batch-size memory impact
* [ ] Sequence-length memory impact

---

# Stage 77 — FP32, FP16, BF16

## Later Topic

## Concepts

* [ ] Number representation
* [ ] Precision
* [ ] Memory consumption
* [ ] Training speed
* [ ] Numerical range

## Connection

A tensor containing the same number of values consumes different amounts of memory depending on dtype.

---

# Stage 78 — CPU vs GPU Tensors

## PyTorch Connection

Later:

```text id="f8vv0y"
CPU tensor
```

and:

```text id="9zyd7p"
GPU tensor
```

represent similar numerical data stored on different hardware.

## Topics

* [ ] Device
* [ ] CPU memory
* [ ] GPU VRAM
* [ ] Data transfer
* [ ] Device mismatch

---

# Stage 79 — Moving Data Between Devices

## Later PyTorch Topic

Topics:

* [ ] CPU → GPU
* [ ] GPU → CPU
* [ ] Transfer cost
* [ ] Why unnecessary transfers reduce performance

---

# Stage 80 — Gradient Tensors

## Model Learning Connection

When a model contains many parameters:

```text id="kxnn68"
parameter tensor
```

gets a corresponding:

```text id="mbwy9h"
gradient tensor
```

with compatible shape.

## Topics

* [ ] Parameter shape
* [ ] Gradient shape
* [ ] One gradient per parameter value
* [ ] Gradient accumulation

---

# Stage 81 — Model Parameter Shapes

## Neural Network Connection

Suppose a linear layer transforms:

```text id="1lwshv"
3 input features
→
5 output features
```

its weight structure must encode connections between those dimensions.

Topics:

* [ ] Input dimension
* [ ] Output dimension
* [ ] Weight matrix
* [ ] Bias vector
* [ ] Shape compatibility

---

# Stage 82 — Activation Tensors

## Topics

* [ ] Intermediate outputs
* [ ] Activations
* [ ] Activation shapes
* [ ] Batch dimension preserved
* [ ] Hidden representations

## Why Important

Training memory contains not only model parameters but also intermediate activations needed for backpropagation.

---

# Stage 83 — Training vs Inference Memory

## Later Systems Topic

During training we often need:

* model parameters,
* gradients,
* optimizer states,
* activations.

During inference:

* gradients are usually unnecessary,
* optimizer state is unnecessary.

## Topics

* [ ] Why training consumes more memory
* [ ] Inference memory
* [ ] Activation memory
* [ ] Gradient memory

---

# Stage 84 — Sequence Windows

## Language Model Data Preparation

Long token streams can be split into training windows.

Example:

```text id="ctjklz"
tokens:
1 2 3 4 5 6 7 8 9

context length = 4
```

Potential windows:

```text id="kdc1ze"
1 2 3 4
2 3 4 5
3 4 5 6
...
```

## Topics

* [ ] Context window
* [ ] Sliding windows
* [ ] Non-overlapping windows
* [ ] Overlapping windows

---

# Stage 85 — Input and Target Shifting for Language Models

## Critical Later Topic

Example:

Input:

```text id="p21a5o"
I love AI
```

Target conceptually:

```text id="vnny5o"
love AI <next>
```

At token level:

```text id="534s25"
input  = [t1, t2, t3, t4]
target = [t2, t3, t4, t5]
```

## Topics

* [ ] Shift input
* [ ] Shift targets
* [ ] Next-token prediction
* [ ] Sequence alignment

---

# Stage 86 — Mini-Batch Language Model Data

Later:

```text id="fbiaub"
inputs:
[batch, sequence]

targets:
[batch, sequence]
```

Each position has a target next token.

This combines:

* tokenizer,
* tensor shapes,
* batches,
* language modeling.

---

# Stage 87 — Masked Positions

## Later Topic

Some objectives train only on selected token positions.

Topics:

* [ ] Ignore index
* [ ] Loss mask
* [ ] Padding mask
* [ ] Selective loss computation

---

# Stage 88 — DataLoader Performance

## Optional Engineering Topic

* [ ] Prefetching
* [ ] Worker processes
* [ ] Pinned memory
* [ ] CPU bottlenecks
* [ ] GPU starvation
* [ ] Throughput

Useful when models become large enough that data loading affects training speed.

---

# Stage 89 — Memory-Mapped Data

## Optional Large-Scale Topic

Large datasets may not fit fully into RAM.

Topics:

* [ ] Memory mapping
* [ ] Streaming data
* [ ] Disk-backed arrays
* [ ] Sequential reads
* [ ] Random access

---

# Stage 90 — Dataset Streaming

## Later LLM Engineering Topic

Topics:

* [ ] Process data without loading everything
* [ ] Streaming batches
* [ ] Remote datasets
* [ ] Shuffle limitations
* [ ] Buffer-based shuffling

---

# Stage 91 — Sharding

## Large-Scale Training Topic

Large datasets may be divided into pieces called shards.

Topics:

* [ ] Dataset shard
* [ ] Parallel loading
* [ ] Distributed workers
* [ ] Avoid duplicate samples across workers

---

# Stage 92 — Distributed Batches

## Later Systems Topic

With multiple GPUs:

```text id="6cc442"
global batch
```

may be divided into:

```text id="64mvsd"
local batches
```

processed independently on different devices.

Topics:

* [ ] Local batch size
* [ ] Global batch size
* [ ] Data parallelism connection

---

# Stage 93 — Gradient Accumulation

## Important Later Topic

If a desired batch is too large for GPU memory:

```text id="bfvjq8"
small batch
↓
calculate gradient
↓
keep gradient
↓
next small batch
↓
add gradient
↓
update later
```

## Topics

* [ ] Micro-batch
* [ ] Accumulated gradient
* [ ] Effective batch size
* [ ] Memory trade-offs

---

# Stage 94 — Token Count as Training Data Size

## LLM Connection

For language models, dataset size is often discussed in:

```text id="qszzl8"
number of tokens
```

rather than only:

```text id="tjlaze"
number of documents
```

Topics:

* [ ] Corpus token count
* [ ] Training token budget
* [ ] Epoch intuition for huge corpora

---

# Stage 95 — Data Mixtures

## Later LLM Topic

Training corpora may combine:

* general web text,
* books,
* code,
* academic material,
* conversations,
* domain-specific datasets.

## Topics

* [ ] Mixture proportions
* [ ] Oversampling
* [ ] Undersampling
* [ ] Domain weighting

---

# Stage 96 — Curriculum Data

## Optional Topic

Training examples can sometimes be ordered or weighted by difficulty or type.

Topics:

* [ ] Curriculum learning intuition
* [ ] Easy-to-hard data
* [ ] Distribution scheduling

---

# Stage 97 — Synthetic Data

## Modern AI Engineering Topic

Data may be generated using models or simulations.

Topics:

* [ ] Synthetic examples
* [ ] Teacher models
* [ ] Data quality
* [ ] Error amplification
* [ ] Filtering synthetic data

---

# Stage 98 — Dataset Versioning

## Engineering Practice

Topics:

* [ ] Dataset version
* [ ] Reproducible experiment
* [ ] Track data changes
* [ ] Training-data metadata

## Goal

Know exactly which data produced which model.

---

# Stage 99 — Data Provenance

## Important Production Topic

Topics:

* [ ] Where data came from
* [ ] Licensing
* [ ] Permissions
* [ ] Source tracking
* [ ] Transformation history

---

# Stage 100 — Data Privacy

## Important Engineering Topic

Topics:

* [ ] Personal information
* [ ] Sensitive information
* [ ] Data minimization
* [ ] Retention
* [ ] Training-data privacy risks

---

# Optional Deep-Dive Topics

These should **not block the main learning path**.

## NumPy Internals

* [ ] Strides
* [ ] Memory layout
* [ ] C-order
* [ ] Fortran-order
* [ ] Views
* [ ] Copies

## Numerical Computing

* [ ] Cache locality
* [ ] SIMD intuition
* [ ] Vectorized native code
* [ ] BLAS overview

## Sparse Data

* [ ] Sparse matrices
* [ ] Dense vs sparse storage
* [ ] Sparse embeddings

## Ragged Tensors

* [ ] Variable-length tensor structures
* [ ] Why dense batching usually uses padding

---

# Practical Exercise Path

## Exercise 001 — NumPy Array Basics

Tasks:

* [ ] Create Python list
* [ ] Convert to NumPy array
* [ ] Inspect type
* [ ] Inspect dtype
* [ ] Perform element-wise arithmetic
* [ ] Compare behavior with Python lists

---

# Exercise 002 — Scalar, Vector, Matrix

Create:

* [ ] scalar
* [ ] vector
* [ ] matrix

For each:

* [ ] inspect value
* [ ] inspect `ndim`
* [ ] inspect `shape`
* [ ] inspect `size`
* [ ] inspect `dtype`

---

# Exercise 003 — Indexing and Slicing

Tasks:

* [ ] select vector element
* [ ] select matrix row
* [ ] select matrix column
* [ ] slice range
* [ ] reverse data
* [ ] select submatrix

---

# Exercise 004 — Axis Operations

Create matrix and calculate:

* [ ] total sum
* [ ] total mean
* [ ] mean across axis 0
* [ ] mean across axis 1
* [ ] compare outputs and shapes

---

# Exercise 005 — Broadcasting

Tasks:

* [ ] vector + scalar
* [ ] matrix + scalar
* [ ] matrix + vector
* [ ] inspect resulting shapes
* [ ] intentionally create incompatible shapes

---

# Exercise 006 — Reshape and Transpose

Tasks:

* [ ] create flat array
* [ ] reshape into matrix
* [ ] flatten again
* [ ] transpose
* [ ] inspect shapes after every operation

---

# Exercise 007 — Dot Product

Tasks:

* [ ] create input vector
* [ ] create weight vector
* [ ] calculate manually
* [ ] calculate using NumPy
* [ ] connect result to neuron prediction

---

# Exercise 008 — Matrix Multiplication

Tasks:

* [ ] create matrices
* [ ] reason about compatible shapes
* [ ] calculate output shape before running code
* [ ] multiply using NumPy
* [ ] inspect result

Main habit:

> Predict the shape first. Run the code second.

---

# Exercise 009 — Dataset Matrix

Build a tiny dataset where:

```text id="ch8je4"
rows = samples
columns = features
```

Tasks:

* [ ] inspect dataset shape
* [ ] select one sample
* [ ] select one feature
* [ ] create target vector

---

# Exercise 010 — Manual Batching

Given a dataset:

* [ ] choose batch size
* [ ] divide samples into batches
* [ ] inspect batch shapes
* [ ] process each batch

---

# Exercise 011 — Train/Validation/Test Split

Tasks:

* [ ] create dataset
* [ ] divide data
* [ ] inspect sizes
* [ ] ensure no overlap

---

# Exercise 012 — Sequence Tensor

Use tokenizer IDs.

Tasks:

* [ ] create one token sequence
* [ ] inspect shape
* [ ] create multiple sequences
* [ ] observe variable lengths

---

# Exercise 013 — Padding

Tasks:

* [ ] create sequences of different lengths
* [ ] choose pad ID
* [ ] pad to common length
* [ ] stack into batch
* [ ] inspect shape

---

# Exercise 014 — Attention Mask

From padded sequences:

* [ ] identify real tokens
* [ ] identify padding
* [ ] create mask
* [ ] inspect token tensor and mask tensor together

---

# Exercise 015 — Embedding Shape Simulation

Before building real embeddings:

Start with:

```text id="yp2fkv"
token_ids shape:
[batch, sequence]
```

Create fake embedding vectors so output becomes:

```text id="asw8zp"
[batch, sequence, embedding]
```

Tasks:

* [ ] inspect every dimension
* [ ] select one sequence
* [ ] select one token
* [ ] select one embedding component

---

# Exercise 016 — Language Model Input/Target Shift

Given token sequence:

```text id="y07di5"
[t1, t2, t3, t4, t5]
```

build:

```text id="o80h0d"
input  = [t1, t2, t3, t4]
target = [t2, t3, t4, t5]
```

Tasks:

* [ ] understand next-token alignment
* [ ] batch multiple sequences

---

# Cross-Track Connections

## Model Learning

Tensors & Data provides:

```text id="qdtgeq"
arrays
↓
multiple samples
↓
batch calculations
↓
multiple parameters
↓
gradient tensors
```

---

## Math for AI

Math explains:

```text id="9iz86u"
scalar
vector
matrix
dot product
matrix multiplication
```

Tensors & Data explains:

> how those mathematical objects are represented and manipulated in code.

---

## Tokenizer

Tokenizer produces:

```text id="j5r1rd"
token IDs
```

Tensors & Data organizes them as:

```text id="gcc86l"
sequence tensors
↓
batches
↓
padding
↓
attention masks
```

---

## Neural Networks

Tensors & Data provides:

```text id="64rk5w"
input vectors
weight matrices
bias vectors
batch dimensions
activation tensors
```

---

## Transformers

This track becomes especially important.

Transformer reasoning depends heavily on understanding:

```text id="a70kxg"
[batch, sequence, hidden]
```

and later:

```text id="r3a5hq"
[batch, heads, sequence, head_dimension]
```

If shapes are understood, transformer code becomes dramatically easier to follow.

---

# Recommended Learning Order

Do **not** complete all 100 stages before continuing other tracks.

Near-term path:

## Phase A — Array Foundations

1. [ ] Python list vs NumPy array
2. [ ] Scalar
3. [ ] Vector
4. [ ] Matrix
5. [ ] Tensor
6. [ ] Dimension
7. [ ] Shape
8. [ ] Axis
9. [ ] dtype

---

## Phase B — Tensor Manipulation

10. [ ] Indexing
11. [ ] Slicing
12. [ ] Element-wise operations
13. [ ] Reductions
14. [ ] Broadcasting
15. [ ] Reshape
16. [ ] Transpose
17. [ ] Concatenation / stacking

---

## Phase C — Linear Algebra in Code

18. [ ] Dot product
19. [ ] Matrix-vector multiplication
20. [ ] Matrix multiplication
21. [ ] Shape reasoning

This directly supports:

* multiple weights,
* first neuron,
* embeddings.

---

## Phase D — Data

22. [ ] Sample
23. [ ] Feature
24. [ ] Target
25. [ ] Dataset
26. [ ] Feature matrix
27. [ ] Batch
28. [ ] Epoch / step
29. [ ] Train / validation / test
30. [ ] Shuffling
31. [ ] Data leakage

---

## Phase E — Language Data

32. [ ] Sequence
33. [ ] Token ID tensor
34. [ ] Sequence length
35. [ ] Variable lengths
36. [ ] Padding
37. [ ] Attention masks
38. [ ] `[batch, sequence]`
39. [ ] `[batch, sequence, embedding]`

---

# Current Position

Already encountered through Model Learning:

* [x] Python lists
* [x] NumPy installation
* [x] `np.array`
* [x] Multiple numerical samples
* [x] Element-wise multiplication
* [x] Element-wise subtraction
* [x] Element-wise squaring
* [x] `np.mean`
* [x] Vectorized prediction
* [x] Vectorized loss calculation

Systematic Tensors & Data track starts here:

```text id="amjdsy"
Python List
↓
NumPy Array
↓
Scalar
↓
Vector
↓
Matrix
↓
Tensor
↓
Shape
↓
Axis
```

Then:

```text id="652m93"
Tensor operations
↓
Dot product
↓
Matrix multiplication
↓
Dataset
↓
Batch
```

Then language-specific data:

```text id="snt9q9"
Token IDs
↓
Sequences
↓
Padding
↓
Batches
↓
Embeddings
↓
Transformer tensors
```

---

# Immediate Next Topics

Priority order:

1. [ ] Python list vs NumPy array
2. [ ] Scalar
3. [ ] Vector
4. [ ] Matrix
5. [ ] Tensor
6. [ ] Dimension
7. [ ] Shape
8. [ ] Axis
9. [ ] Indexing
10. [ ] Element-wise operations
11. [ ] Broadcasting
12. [ ] Dot product
13. [ ] Matrix multiplication
14. [ ] Dataset
15. [ ] Batch

---

# Completion Goal

This track reaches foundation-level completion when tensor code can be read by thinking about the underlying data structure rather than memorizing library syntax.

For example, seeing:

```text id="s42sh9"
[32, 128, 768]
```

should immediately suggest:

```text id="p1x9xk"
32 samples/sequences
128 positions per sequence
768 numerical features per position
```

and when an operation happens, the first questions should naturally become:

```text id="732voo"
What does each dimension represent?
What are the input shapes?
Which axis is being operated on?
What should the output shape be?
```

That ability will later make neural-network, PyTorch, and transformer code much easier to reason about.
