## This is a ML project


In this project, I have developed a basic content-based recommendation system for 5000 Tmdb movies list. This begins with a gentle introduction to content-based recommendation systems and the underlying concepts. Further, I will be performing basic Exploratory Data Analysis (EDA) before going on to build the recommendation system.

Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.

I have used text vectorization used in NLP.
Processing natural language text and extract useful information from the given word, a sentence using machine learning and deep learning techniques requires the string/text needs to be converted into a set of real numbers (a vector) — Word Embeddings.

Word Embeddings or Word vectorization is a methodology in NLP to map words or phrases from vocabulary to a corresponding vector of real numbers which used to find word predictions, word similarities/semantics.

The process of converting words into numbers are called Vectorization. I have used a method called CountVectorizer available in Scikit-learn to do this process.

After the words are converted as vectors, we need to use some techniques such as Euclidean distance, ##### Cosine Similarity to identify similar words.

Count the common words or Euclidean distance is the general approach used to match similar documents which are based on counting the number of common words between the documents.This approach will not work even if the number of common words increases.To overcome this flaw, the “Cosine Similarity” approach is used to find the similarity.

Mathematically, it measures the cosine of the angle between two vectors (item1, item2) projected in an N-dimensional vector space. The advantageous of cosine similarity is, it predicts the document similarity even Euclidean is distance.


### FInally after creating the model, we pickled the model and made an app through streamlit.








