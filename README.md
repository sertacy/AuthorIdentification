
<img src="src/youoryou.jpg" width="340">

# Author Identification

## Introduction:

**Goal of this task:**
Implement, optimize, and evaluate a tool for author identification.  
→ Given two texts, decide whether the author is the same.  
**Approach:** Analyze writing styles and other attributes of texts.

---

## Motivation:

Working with large datasets of anonymous text (e.g., the internet) makes author identification a   
very important task, crucial for fields such as forensics, security, and marketing.

---

## Classifier:

Choices include Linear Regression (Maximum Entropy) and various Support Vector Machines techniques.  
Different classifiers can have varying accuracy depending on the task and data.

**Best classifier for this project:** LinearSVM

---

## Data Preparation:

*   Copying and renaming all training files to: `"[number of file][known/unknown].txt"` using `Copy.py`.
*   Creating a list consisting of sentences (each line of text as an individual element).

---

## Length Features:

*   Average length of words (in characters)
*   Average sentence length (in characters)
*   Average sentence length (in words)

---

## Text Features:

*   Count of empty lines

---

## Sentiment Features:

*   Average frequency of positive adjectives in text
*   Average frequency of negative adjectives in text
*   Average frequency of sentiment adjectives in text

**Sidenote:** These were some of the best features for the previous task: sentiment classification.

---

## Evaluation:

Given very few examples of tagged data, evaluation was done manually for the development data (size: 10-20 classification tasks).  
Training data and development data were always varied, leading to a manual application of k-fold evaluation.

**Results:** Average F1-Score over 80% (depending on fold size).

---

## Usage of Program (Manual):

The program uses all 100 text pairs to train classifiers. Directories of the two text files are input through the console.  
Prediction is saved in the text document `prediction.txt` ("Y" means same author, "N" means different authors).

---

## Possibilities for Improvement:

*   Using a larger dataset (in this task: only 100 tagged examples were given).
*   Expanding features with the help of linguistic knowledge (interdisciplinary cooperation).
*   Learning about other classifying techniques and applying them to this task.

---


# Abstract: Author Identification

The goal of this project was to implement, optimize, and evaluate a tool for author identification. It identifies the author of a text by analyzing the writing style and other attributes of the text. Given two text files, my tool will decide if both text files are from the same author or not.

This project presents an interesting task due to its potential uses for various problems. A tool with these abilities could be useful for anyone working with large amounts of anonymous text data (e.g., from the internet). It would help identify who exactly, or what kind of person, wrote a text passage online based solely on the text itself. Such identification, verification, and profiling tools are of growing importance in forensics, security, and marketing.

The tool is written in Python and uses a machine learning technique called "Support Vector Machines." The challenge of the project was to find criteria (features) that identify a specific author, to train our machine learning algorithm on this basis. Since I am working with raw text data, this implementation can easily be adapted for other examples by providing two files: one with some text from a known author and another with text from an unknown author.

**Used data:** Training corpus PAN15-Authorship-Verification-Training-Dataset (English).
**External libraries:** I used/tested scikit-learn's Linear Support Vector Classifier, Support Vector Classifier, and the Linear Model - Logistic Regression.
**Data preparation:** For better handling of the given corpus data, I wrote and used `copy.py` to copy and prepare known-author / unknown-author data into one folder, saved as related files.

As features for the classification, I extracted text length, newline count, sentence length, word length, positive sentiment frequency, negative sentiment frequency, and sentiment frequency data.

Because I only had a small excerpt of text for each author and only 100 already predicted cases, this task can easily be optimized by increasing the given text data and by adding more features. Therefore, while the current prediction results are representative for the amount of given examples and demonstrate the concept of author identification, the accuracy of the prediction can easily be increased with bigger data. This shows that even with simple features, it is possible to identify distinctive writing styles.

**References:**
*   http://www.uni-weimar.de/medien/webis/events/pan-15/pan15-web/author-identification.html
*   http://scikit-learn.org/
