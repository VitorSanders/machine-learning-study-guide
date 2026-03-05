# Module 1 – Computer Science Fundamentals 💻

> *"Everyone should know how computers work; it’s not magic, just a lot of logic."*  
>
> — Adapted from a famous quote by Donald Knuth

Welcome to the first chapter of your machine learning journey. This module serves as the foundation; without a solid grasp of these fundamentals, later topics will feel opaque. Think of this as a gentle introduction to the way computers think and to the basic tools you’ll use to instruct them.

---

## 1.1 What Is a Computer?
A computer is an electronic device that **takes input, processes it, and produces output**. At the heart of every modern machine is a CPU (Central Processing Unit) that performs arithmetic and logical operations, and memory where data and instructions are stored.

### 1.1.1 Downloading the IMDB Dataset
Before we start using the IMDB data in examples and deliveries, you’ll need a local copy. The dataset is publicly available in several formats; for simplicity we’ll work with the "title.basics" CSV/TSV file.

1. Visit the IMDB datasets page: https://datasets.imdbws.com/
2. Click on **`title.basics.tsv.gz`** to download the compressed file.
3. Extract the archive (PowerShell example):
   ```powershell
   tar -xzf title.basics.tsv.gz   # after installing a tar utility
   # or use 7‑Zip / Windows Explorer to extract
   ```
4. Move the resulting `title.basics.tsv` (or convert to CSV) into a `data/` folder at the root of this repository.

> ✨ For the early modules you can also create a small sample manually (e.g. `imdb_sample.csv`) with a handful of rows; we don’t need the full dataset right away. Just ensure the file lives under `data/` so our scripts know where to look.

This step only needs to be done once; later modules will assume the data file is available locally under `data/`.

---

### 1.1.2 Binary Numbers
Computers operate using binary—strings of 0s and 1s. Each digit is called a *bit*. Eight bits make a *byte*, which is enough to represent a single character (like `'A'`).

**Example:**
```
Decimal  Binary
0        0000
1        0001
2        0010
3        0011
4        0100
```

### 1.1.3 CPU and Memory
- **CPU** executes instructions one at a time, fetching them from memory.
- **RAM** (Random Access Memory) holds the data and code the CPU is currently using.

Visualize memory as numbered boxes; each can store a value.

---

## 1.2 Data Types and Storage
Computers categorize values by type. Python, our language of choice, is dynamically typed, but understanding the underlying concepts is crucial.

### 1.2.1 Primitive Types
- **Integers** (`42`, `-7`)
- **Floating-point numbers** (`3.14`, `-0.001`)
- **Strings** (`"hello"`), sequences of characters
- **Booleans** (`True`, `False`)

Internally, integers and floats are stored in binary with fixed bit widths; strings are arrays of bytes using encodings like UTF-8.

### 1.2.2 Compound Types
- **Lists** – ordered collections: `[1, 2, 3]`
- **Dictionaries** – key/value stores: `{"title": "Inception", "year": 2010}`

These structures let us group related data. A list of movie titles from the IMDB dataset is a common starting point.

---

## 1.3 Control Flow
Logical decisions and repetition allow us to write programs that react and iterate.

### 1.3.1 Conditionals
```python
rating = 8.7
if rating >= 8.0:
    print("That's a great movie!")
elif rating >= 5.0:
    print("It's okay.")
else:
    print("Consider skipping it.")
```

The `if` statement tests conditions; the first truthy branch executes.

### 1.3.2 Loops
Loops repeat blocks of code.

**For loop (iterate list):**
```python
movies = ["The Matrix", "Titanic", "Avatar"]
for title in movies:
    print(title)
```

**While loop (conditional repetition):**
```python
count = 0
while count < 3:
    print("count is", count)
    count += 1
```

Use loops to process rows of a dataset or repeatedly query a user.

---

## 1.4 Functions and Modular Thinking
Functions are reusable blocks of code that accept parameters and may return a value.

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)  # 15
```

Breaking a program into functions keeps your code organized and easier to test.

### 1.4.1 Example: Parsing Movie Titles
```python
def load_titles(path):
    titles = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            # assume CSV: title,year,rating
            parts = line.strip().split(',')
            titles.append(parts[0])
    return titles

all_titles = load_titles('imdb_sample.csv')
print(all_titles[:5])
``` 

Modularity lets you swap `load_titles` for a version that reads from a real IMDB file without rewriting the rest.

---

## 1.5 Exercises
1. **Binary conversion:** Write functions `to_binary(n)` and `from_binary(s)`.
2. **Conditional script:** Ask the user for a movie rating and print a recommendation.
3. **Loop practice:** Read a small list of movie titles and print those released before 2000.
4. **Function practice:** Implement `average_rating(ratings)` and test it with sample data.

Each exercise should be saved in its own `.py` file and run from the command line.

---

## 1.6 Delivery: IMDB Slice Parser
Build a Python script that:
- Opens a provided IMDB CSV/TSV excerpt
- Extracts and prints the movie titles using loops and conditionals

You don’t need external libraries yet. Focus on file I/O and string manipulation. When finished, commit the script to your repository and include a short README describing how to run it.

> Tip: This script will serve as a template for later modules when we add `pandas` and other tools.

---

## 1.7 Further Reading & References
- [Python documentation on control flow](https://docs.python.org/3/tutorial/controlflow.html)
- Chapter 1 of "Automate the Boring Stuff with Python" by Al Sweigart
- Khan Academy’s [Intro to computing](https://www.khanacademy.org/computing)


---

*With these concepts in hand, you're ready to move on to writing real Python programs. The next module will deepen your Python skills and introduce libraries that make data work easier.*