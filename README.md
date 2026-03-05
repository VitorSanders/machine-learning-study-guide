# Machine Learning Study Guide 📘

Welcome to a comprehensive study guide designed for learners with **no prior computer science or programming experience**. The goal is to take you from the very basics all the way to senior‑level machine learning concepts, using the **public IMDB dataset** as a recurring example for hands‑on projects and deliveries.

---

## 🎯 Who Is This For?
This guide is written for absolute beginners—whether you're completely new to computers or you have some familiarity but want a structured path into machine learning. Every module includes clear explanations, suggested exercises, and a delivery (mini‑project) based on IMDB data so you can apply what you learn.

## 📚 How to Use This Guide
1. **Follow modules in order** – each builds on the previous.
2. **Do the exercises** – practice is key for retention.
3. **Complete the deliveries** – each module ends with a mini‑project using IMDB data.
4. **Refer back** when you encounter new problems in your projects.

---

## 🧩 Module Overview


### [Module 0 – Setup & Tools 🛠️](modules/module0.md)
**What you’ll learn:**
- Installing Python 3 & package manager (pip)
- Choosing and configuring an IDE/text editor (VS Code recommended)
- Using Git/GitHub for version control
- Navigating the command line (Windows PowerShell basics)

**Resources:**
- Python installation guide (docs.python.org)
- GitHub Hello World tutorial
- VS Code documentation for Python

**Delivery:**
- Create a GitHub repository and upload a simple `hello_world.py` script.

---

### [Module 1 – Computer Science Fundamentals 💻](modules/module1.md)

**What you’ll learn:**
- What a computer actually does (binary, CPU, memory)
- Basic data types (numbers, strings, lists) and how computers store them
- Control flow: conditionals (`if`/`else`) and loops (`for`, `while`)
- Functions and modular thinking

**Resources:**
- "Automate the Boring Stuff with Python" (ch.1)
- Khan Academy intro to computing

**Delivery:**
- Write Python scripts that parse a small slice of the IMDB dataset (e.g. list movie titles) using loops and conditionals.

---

### [Module 2a – Python Basics 🐍](modules/module2a.md)

**What you’ll learn:**
- Variables, expressions, and basic operators
- Strings, lists, and writing simple functions
- Simple I/O using `input()` and `print()`
- Writing and running Python scripts from the command line

**Resources:**
- Python official tutorial (sections 1-3)
- Codecademy Python course (free portion)

**Delivery:**
- Create a small command‑line program that interacts with the user (e.g., a movie rating quiz).

---

### [Module 2b – Python for Data 💾](modules/module2b.md)

**What you’ll learn:**
- Working with files, reading/writing CSV and TSV
- Introduction to `numpy` and `pandas`
- Creating and using virtual environments
- Error handling and basic debugging techniques

**Resources:**
- "Python for Data Analysis" by Wes McKinney (ch.1)
- pandas official getting started page

**Delivery:**
- Load the full IMDB CSV into `pandas`, perform simple queries (e.g. top 10 rated movies) and save the results to new files.

---

### [Module 3 – Data Handling & Visualization 📊](modules/module3.md)
**What you’ll learn:**
- Data cleaning and preprocessing (missing values, normalization)
- Feature engineering (extracting useful attributes from text, dates, etc.)
- Exploratory data analysis (EDA) with visualizations
- Storing and loading processed datasets for reuse

**Resources:**
- seaborn tutorial
- "Practical Statistics for Data Scientists"

**Delivery:**
- Prepare an IMDB dataset for modeling: clean titles, encode categories, and create a notebook summarizing your EDA findings with charts.

---

### [Module 4 – Math Foundations 📐](modules/module4.md)
**What you’ll learn:**
- Linear algebra essentials (vectors, matrices, dot products)
- Calculus basics (derivatives, gradients) with intuitive examples
- Probability & statistics (mean, variance, distributions, Bayes’ theorem)
- Why these topics matter in machine learning

**Resources:**
- 3Blue1Brown "Essence of Linear Algebra" series
- Khan Academy calculus and statistics

**Delivery:**
- Compute basic statistics on IMDB ratings and visualize distributions using `matplotlib` or `seaborn`.

---

### [Module 5 – Introduction to Machine Learning 🤖](modules/module5.md)
**What you’ll learn:**
- Supervised vs unsupervised learning
- Common algorithms: linear regression, decision trees, k-nearest neighbours
- Model training, testing, and evaluation metrics (accuracy, RMSE, confusion matrix)
- Overfitting and generalization

**Resources:**
- Andrew Ng’s Coursera ML course (videos)
- "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" (early chapters)

**Delivery:**
- Build a simple classifier on IMDB data to predict genre or rating class. Train/test split and evaluate performance. Document results.

---

### [Module 6 – Deep Learning Basics 🧠](modules/module6.md)
**Estimated time:** 4–6 weeks

**What you’ll learn:**
- Neural network fundamentals (layers, activation functions, loss functions)
- Using frameworks like TensorFlow/Keras or PyTorch
- Training deep models and monitoring with TensorBoard or equivalent
- Handling text data with embeddings and recurrent networks

**Resources:**
- TensorFlow/Keras official tutorials
- "Deep Learning with Python" by François Chollet

**Delivery:**
- Create a neural network that takes movie plots (text) from IMDB and predicts the genre or sentiment. Use word embeddings and evaluate accuracy.

---

### [Module 7 – Advanced Topics & Best Practices 🚀](modules/module7.md)
**What you’ll learn:**
- Natural language processing (NLP) techniques for classification and information retrieval
- Model evaluation in depth: precision, recall, F1 score, ROC curves
- Hyperparameter tuning and validation strategies (cross‑validation, grid search)
- Basics of deployment (saving models, simple web API with Flask/FastAPI)

**Resources:**
- FastAPI documentation
- scikit-learn model evaluation guide

**Delivery:**
- **Phase 1:** Train and evaluate a sentiment model on IMDB data.
- **Phase 2:** Learn basic web frameworks like Flask or FastAPI.
- **Phase 3:** Wrap your model in an API and deploy it locally or on a free hosting service. Include a README with usage instructions.

---

### [Module 8 – Senior Machine Learning & Research 🧩](modules/module8.md)
**Estimated time:** 4–6 weeks

**What you’ll learn:**
- Reading and understanding research papers
- Optimization techniques (Adam, RMSprop, learning rate schedules)
- Scaling models with GPUs and distributed training
- Ethical considerations and reproducibility in ML research

**Resources:**
- arXiv.org for research papers
- "The Hundred-Page Machine Learning Book" (for concise summaries)

**Delivery:**
- Choose a recent ML paper (related to NLP or recommendation systems). Reproduce key experiments on the IMDB dataset and write a report summarizing findings, challenges, and improvements.

---

## 📘 Glossary
A quick reference for terms that come up throughout the guide. Don’t worry if you don’t remember all of these at first; you can revisit this section whenever you see a word you don’t understand.

- **Algorithm:** a step‑by‑step procedure for solving a problem.
- **Dataset:** a collection of structured information (e.g. the IMDB movie records).
- **Gradient:** vector of partial derivatives indicating the slope of a function.
- **Hyperparameter:** a configuration value set before training (e.g. learning rate).
- **Normalization:** scaling data to a specific range.
- **Overfitting:** when a model learns noise rather than signal, performing poorly on new data.
- **Training set / Test set:** subsets of data used to build and evaluate models, respectively.


---

## 📝 Additional Resources
- Official Python tutorials: https://docs.python.org/3/tutorial/
- MIT OpenCourseWare (Intro to Computer Science & Algorithms)
- 3Blue1Brown’s videos on linear algebra and calculus
- Coursera, edX, or Udacity machine learning courses for structured study

## 🎓 Final Notes
Each module builds practical skills through explanation and real IMDB‑based practice. Keep your code in version control, write clear documentation, and don’t hesitate to revisit earlier modules as you progress. Machine learning is a journey—enjoy the learning process! 😊

---

*Happy studying!*
