# Author Identification


## Introduction:

Goal of this task  

Implement, optimize and evaluate a tool for author identification  

→ Given 2 texts decide whether author is same  

Approach: Analyze writing styles and other attributes of texts

_________________

## Motivation:

working with big data of anonymous text (e.g. internet) →  
very important task to identify author of specific text as well important for fields such as forensics, security and marketing.

_________________

## Classifier:

Choice between Linear Regression (Maximum Entropy) and various Support Vector Machines techniques.    
Different classifiers can have varying accuracy depending on task and data.  

Best classifier for this project: LinearSVM 

__________________

## Data Preparation:

Copying and renaming all training files to:  
„[number of file][known/unknown].txt“

with Copy.py   

Creating a list consisting of sentences  
(each line of text as individual element)

__________________

## Length Features:

average length of words (in chars)  
average sentence length (in chars)  
average sentence length (in words)  

_________________________

## Text Features:

count of empty lines

_________________________

## Sentiment Features:

average frequency of positive adjectives in text  
average frequency of negative adjectives in text  
average frequency of sentiment adjectives in text  

Sidenote:  
these are some of the best features for the previous task: sentiment classification

________________________

## Evaluation:

Very very few given examples of tagged data  
Evaluation was done manually for the development-data  
(size: 10-20 classification tasks)  
Training-data and development-data were always varied  
→ manual application of k-fold evaluation  

Results: Average F1-Score over 80% (depending on foldsize)  

_________________________

## Usage of program (Manual):

Program uses all 100 text pairs to train classifiers  
Directories of the two textfiles → input through the console  
Prediction is saved in the textdocument prediction.txt  
(„Y“ means same author, „N“ means different authors)  

____________________________

## Possibilites for improvement:

Using bigger data (in this task: only 100 tagged examples were given)   
Expand features with help of linguistic knowledge (interdisciplinary cooperation)    
Learn about other classifying techniques → apply to this task  

_____________________________
_____________________________
_____________________________
_____________________________
_____________________________
_____________________________

# Abstract: Author Identification

The goal of the project was to implement, optimize and evaluate a tool for author 
identification.It identifies the author of a text by analyzing the writing style and other 
attributes of the text. Given two text-files, my tool will decide, if both text-files are from
the same author or not.  

This project provides an interesting task, because of the use it could be for certain 
problems. A tool with these abilities could be useful for someone who is working 
with a lot of anonymous text data, e.g. the internet, and will help to identify, who 
exactly or what kind of person wrote a text passage on the internet based on the text 
itself. Such identification, verification and profiling tools are of growing importance in 
forensics, security, and marketing.  

The tool is written in Python and uses a machine learning technique called "Support 
Vector Machines". The challenge of the project was to find criteria(features) which 
identify a specific author, to train our machine learning algorithm on this basis. Since 
I am working with raw text-data, this implementation can easily be adopted for other
examples, by providing two files, one file with some text from the author and another 
file with the text from the unknown author.   

Used data: Training corpus PAN15-Authorship-Verification-Training-Dataset (English)
External libraries: I have used/tested scikit-learns Linear Support Vector Classifier , 
Support Vector Classifier and the Linear Model - Logistik Regression.
Data preparation: For better handling of the given corpus data I have written and 
used a copy.py to copy and prepare known-author / unknown-autor data in one folder 
saved as related files.  

As features for the classification I have extracted text length, newline count, 
sentence length, word length, positive sentiment frequency, negative sentiment 
frequency and sentiment frequency data.  

Because I only had a small excerption of text for each author and have only 100 
already precited cases, this task can easily be optimized by increasing the given text 
data and by adding more features. So the results of the predictions will be 
represantative for the amount of given examples and show the concept of author 
identification, but the accuracy of the prediction can easily be increased with bigger 
data. This shows that even with simple features it is possible to identify distinctive 
writing styles.   

References:   
http://www.uni-weimar.de/medien/webis/events/pan-15/pan15-web/author-identification.html  
http://scikit-learn.org/  
