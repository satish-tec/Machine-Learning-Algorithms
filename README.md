# Machine Learning Algorithms Repository

## 📁Overview
This repository contains implementations of fundamental **Machine Learning** algorithms used for **Concept Learning** in hypothesis space search. The algorithms included are:

- **Find-S Algorithm**
- **List-Then-Eliminate Algorithm**
- **Candidate Elimination Algorithm**

These algorithms are used in machine learning to derive hypotheses from training data, particularly for binary classification problems.

---

## 📖Algorithms Explained

### 1. Find-S Algorithm
**Find-S (Finding the most specific hypothesis)** is a simple algorithm used to find the most specific hypothesis that fits the given set of positive training examples. It starts with the most specific hypothesis and generalizes it as needed.

#### **Logic:**
1. Initialize the hypothesis `h` to the most specific value (`⟨?, ?, ?, ..., ?⟩`).
2. For each positive training example:
   - Compare it with `h`.
   - Generalize `h` only where necessary to match the example.
3. Ignore negative examples (Find-S only works for positive instances).
4. The final hypothesis is the most specific one that fits all positive instances.

#### **Limitation:**
- Only works for linearly separable data.
- Cannot handle noise or negative examples.

---

### 2. List-Then-Eliminate Algorithm
The **List-Then-Eliminate** algorithm finds the correct hypothesis by maintaining a list of all possible hypotheses and eliminating those that contradict the training data.

#### **Logic:**
1. Start with a list of all possible hypotheses.
2. For each training example:
   - Remove hypotheses that do not match the example.
3. At the end, the remaining hypotheses are consistent with the training data.

#### **Limitation:**
- Computationally expensive for large hypothesis spaces.
- Requires exhaustive enumeration of hypotheses.

---

### 3. Candidate Elimination Algorithm
The **Candidate Elimination** algorithm finds both the most specific (`S`) and most general (`G`) hypotheses that are consistent with the training data.

#### **Logic:**
1. Initialize the **S** set with the most specific hypothesis (`⟨∅, ∅, ..., ∅⟩`).
2. Initialize the **G** set with the most general hypothesis (`⟨?, ?, ..., ?⟩`).
3. For each training example:
   - If positive:
     - Generalize `S` minimally to include the example.
     - Remove `G` elements that do not include the example.
   - If negative:
     - Specialize `G` minimally to exclude the example.
     - Remove `S` elements that include the example.
4. Continue until no more training examples exist.

#### **Advantage:**
- Finds the complete hypothesis space.
- Handles noise and negative examples better than Find-S.

#### **Limitation:**
- Computationally expensive.
- Large hypothesis spaces can make the algorithm slow.

---

## 📝Installation & Usage

### 📌Prerequisites
- Python 3.x
- Required libraries: `numpy`, `pandas`

## 🚀 How to Use
### Clone the Repository
```bash
$ git clone https://github.com/satish-tec/machine-learning-algorithms.git
$ cd machine-learning-algorithms
```

### Running the Algorithms
To run each algorithm:

```bash
$ python FindSAlgorithm.py  # Run Find-S Algorithm
$ python list_then_eliminate.py  # Run List-Then-Eliminate Algorithm
$ python candidate_elimination.py  # Run Candidate Elimination Algorithm
```
Modify the datasets and experiment with different training examples.

### Example Input Format
Data should be in CSV format with the last column as the class label (positive/negative).

```csv
Sunny, Warm, Normal, Strong, Warm, Same, Yes
Sunny, Warm, High, Strong, Warm, Same, Yes
Rainy, Cold, High, Strong, Warm, Change, No
```

---

### 📚References

Tom M. Mitchell, Machine Learning, McGraw Hill, 1997.

## 🎯Contributing
Feel free to fork and submit pull requests. Contributions are welcome!

## 📝License
This repository is licensed under the MIT License.
