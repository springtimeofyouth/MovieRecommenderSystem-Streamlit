# Movie Recommendation System with Streamlit

In this project, I have developed a basic content-based recommendation system for 5000 Tmdb movies list. This begins with a gentle introduction to content-based recommendation systems and the underlying concepts. Further, I will be performing basic Exploratory Data Analysis (EDA) before going on to build the recommendation system.

Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.

I have used text vectorization used in NLP.
Processing natural language text and extract useful information from the given word, a sentence using machine learning and deep learning techniques requires the string/text needs to be converted into a set of real numbers (a vector) — Word Embeddings.

Word Embeddings or Word vectorization is a methodology in NLP to map words or phrases from vocabulary to a corresponding vector of real numbers which used to find word predictions, word similarities/semantics.
The process of converting words into numbers are called Vectorization. I have used a method called CountVectorizer available in Scikit-learn to do this process.
After the words are converted as vectors, we need to use some techniques such as Euclidean distance, Cosine Similarity to identify similar words.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Acknowledgments](#Acknowledgements)
- [Future Prospect](#FutureProspect)

## Introduction
Developed a basic content-based recommendation system for 5000 Tmdb movies list.Used text vectorization used in NLP. And Finally created an UI using Streamlit.

## Dependencies

Make sure you have the following dependencies installed:

- [NumPy](https://numpy.org/): Used for numerical operations in Python.
- [Pandas](https://pandas.pydata.org/): Provides data structures for efficiently storing and manipulating large datasets.
- [scikit-learn](https://scikit-learn.org/): A machine learning library that provides simple and efficient tools for data analysis and modeling.
- [Matplotlib](https://matplotlib.org/): A plotting library for creating static, animated, and interactive visualizations in Python.
- [Streamlit](https://streamlit.io/): A Python library for creating web applications with minimal code.
- [Kneed](https://github.com/arvkevi/kneed): A knee-point detection algorithm implementation.
- [Seaborn](https://seaborn.pydata.org/): A data visualization library based on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.
- [NLTK](https://www.nltk.org/): Natural Language Toolkit for working with human language data.
- [pipreqs](https://github.com/bndr/pipreqs): A tool that generates the requirements.txt file based on the imports in your Python script.


Install the dependencies using the following command:

```bash
pip install -r requirements.txt

```
## Usage
```
git clone https://github.com/your-username/neural-style-transfer.git

python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

pip install -r requirements.txt

````
- Run the jupyter notebook

- Go to terminal and write

```
 streamlit app.py
```

## FutureProspect

Since the pickle file created for this is larger than 100 mb. It is not deployed. In future, remote access to the pickle file and the app will be deployed.
However, the app will run finely in localhost.

## Acknowledgements
- This project is inspired by the Video on YouTube Channel name (CampusX).[Link]([https://youtu.be/1xtrIEwY_zY?si=Ntgr38P5zR5gdbYw])
