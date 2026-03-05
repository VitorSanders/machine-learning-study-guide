# Module 1 – Computer Science Fundamentals 💻

> *"Everyone should know how computers work; it’s not magic, just a lot of logic."*
>
> — (adapted quote)

**Resources:**
- "Automate the Boring Stuff with Python" (ch.1)
- Khan Academy intro to computing

Welcome to the first chapter of your machine learning journey. This module serves as the foundation; without a solid grasp of these fundamentals, later topics will feel opaque. Think of this as a gentle introduction to the way computers think and to the basic tools you’ll use to instruct them.

---

## 1.1 What Is a Computer?
A computer is an electronic device that **takes input, processes it, and produces output**. At the heart of every modern machine is a CPU (Central Processing Unit) that performs arithmetic and logical operations, and memory where data and instructions are stored. Later, when you build models, you’ll feed numbers into the computer and it will transform them according to your code – understanding this cycle helps demystify the tools you’re learning.

### 1.1.2 CPU and Memory
- **CPU** executes instructions one at a time, fetching them from memory.
- **RAM** (Random Access Memory) holds the data and code the CPU is currently using.

Think of RAM as the desk you’re working on right now: you can quickly grab a notebook or calculator on your desk. Your hard drive or SSD, by contrast, is like a filing cabinet where you keep documents you’re not actively using. When you run a program, the computer moves it from the "filing cabinet" into the RAM desk so the CPU can access it fast.

Visualize memory as numbered boxes; each can store a value.

---

### 1.1.3 Binary Numbers
Computers operate using binary—strings of 0s and 1s. Each digit is called a *bit*. Eight bits make a *byte*, which is enough to represent a single character (like `'A'`). Every piece of data, from the letters in a movie title to the numerical rating you give a film, is ultimately stored as binary inside the computer.

Knowing this isn’t strictly necessary to write Python, but it helps explain why numbers behave the way they do and why machine learning algorithms operate on arrays of numbers under the hood.

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
Computers categorize values by type. Python, our language of choice, figures out the type automatically when you assign a value, which is what "dynamically typed" means. You don’t have to declare the type ahead of time; Python does it for you. Understanding the types helps you know what operations are allowed on different pieces of data.

### 1.2.1 Primitive Types
- **Integers** (`42`, `-7`) – whole numbers. You can add, subtract, multiply, etc.
  ```python
  a = 5
  b = 2
  print(a + b)  # 7
  ```
- **Floating-point numbers** (`3.14`, `-0.001`) – numbers with a decimal point.
  ```python
  pi = 3.14
  print(pi * 2)  # 6.28
  ```
- **Strings** (`"hello"`), sequences of characters.
  ```python
  title = "Inception"
  print(title[0])  # I
  ```
- **Booleans** (`True`, `False`) – used for yes/no logic.
  ```python
  is_good = True
  ```

Internally, integers and floats are stored in binary with fixed bit widths; strings are arrays of bytes using encodings like UTF-8.

### 1.2.2 Compound Types
- **Lists** – ordered collections: `[1, 2, 3]`. You can loop over them.
  ```python
  movies = ["Matrix", "Titanic"]
  for m in movies:
      print(m)
  ```
- **Dictionaries** – key/value stores: `{"title": "Inception", "year": 2010}`. Useful for keeping related properties together.
  ```python
  film = {"title": "Inception", "year": 2010}
  print(film["title"])  # Inception
  ```

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
Functions are reusable blocks of code that accept parameters and may return a value. The idea is to break a task into small pieces so you can test and reuse them.

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)  # 15
```

Breaking a program into functions keeps your code organized and easier to test.

### 1.4.1 Example: Parsing Movie Titles
Here’s a simple function that reads a CSV file containing movie data and returns a list of titles. The details are not important yet; focus on the fact that the code is wrapped in a function.

```python
def load_titles(path):
    titles = []
    # open the file and read each line
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            # assume CSV: title,year,rating
            parts = line.strip().split(',')  # split the line into pieces
            titles.append(parts[0])         # take the first piece (the title)
    return titles

all_titles = load_titles('imdb_sample.csv')
print(all_titles[:5])
```

- `with open(...) as f:` opens a file and gives you a variable `f` to read from. The `with` ensures it’s closed afterward.
- `.strip()` removes the newline at the end of the line.
- `.split(',')` turns the line into a list of values separated by commas.

The important idea: the function does a job (loading titles) and the rest of your program can call it without worrying how it works.

---

## 1.5 Exercises
1. **Loop practice:** Read the list of movie titles you used earlier and print those released before 2000. (Hint: use a `for` loop and an `if` statement.)
2. **Conditional script:** Ask the user for a movie rating and print a recommendation using `if`/`else`.
3. **Function practice:** Implement `average_rating(ratings)` that takes a list of numbers and returns their average. Test it with sample data.
4. **Binary conversion (challenge):** Write functions `to_binary(n)` and `from_binary(s)` that convert between decimal integers and binary strings. If this feels hard, try drawing the process on paper first and step through small numbers.

Each exercise should be saved in its own `.py` file and run from the command line. You can start with the easier tasks and come back to the binary challenge when you’re ready.

---

## 1.6 Delivery: IMDB Slice Parser
Build a Python script that:
- Opens a small excerpt of the IMDB CSV/TSV file (use the sample you created earlier or manually make a file called `imdb_sample.csv` with 5‑10 rows).
- Extracts and prints the movie titles using loops and conditionals.

You don’t need external libraries yet. Focus on file I/O and string manipulation. When finished, commit the script to your repository and include a short README describing how to run it. The dataset download from the earlier (module 0) instructions or your hand‑made sample can serve as the source.

> Tip: This script will serve as a template for later modules when we add `pandas` and other tools.


---

## 1.7 Further Reading & References
- [Python documentation on control flow](https://docs.python.org/3/tutorial/controlflow.html)
- Chapter 1 of "Automate the Boring Stuff with Python" by Al Sweigart
- Khan Academy’s [Intro to computing](https://www.khanacademy.org/computing)


---

*With these concepts in hand, you're ready to move on to writing real Python programs. The next module (Python basics) will introduce variables, strings, lists and simple I/O to give you hands‑on practice before we start working with data libraries.*