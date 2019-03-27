#!/usr/bin/env python
# coding: utf-8

# In[124]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import math 

math.log10(10)


# In[116]:


# loading the data set
data = pd.read_csv("train.tsv", sep = '\t')


# In[117]:


train = data['title'].values
# we just take the first 50 line


# In[118]:


# for simplicity we take first 50 lines
train_bin = train[:4]
print(train_bin)


# In[119]:


vectorizer = CountVectorizer()
x_train = vectorizer.fit_transform(train_bin)
x_train.toarray()


# In[120]:


#vectorizer.fit(train_bin[:3])


# In[153]:


# we take top 10 max word for binary freq

def word_to_index(vocab):
    word_to_ind = {}
    i = 0
    for w, count in vocab.items():
        word_to_ind[w] = i
        i += 1
    return word_to_ind

def lower_bound_frq(data):
    vectorizer = CountVectorizer()
    x_train = vectorizer.fit(data)
    vocab = x_train.vocabulary_
    
    matrix = []
    word_to_in =  word_to_index(vocab)
    
    for sentence in data:
        temp = CountVectorizer()
    
        temp_data = temp.fit([sentence])
        temp_vocab = temp_data.vocabulary_
        vector = np.zeros(len(vocab))
        
        for word, freq in temp_vocab.items():
            # we add 1 in freq as vocabulary didn't include word itself when counting the occurences 
            if freq+1 >= 5:
                vector[word_to_in[word]] = 1
            
            
        
        matrix.append(vector)
        print(vector)
    
def caped_frq(data):
    vectorizer = CountVectorizer()
    x_train = vectorizer.fit(data)
    vocab = x_train.vocabulary_
    
    matrix = []
    word_to_in =  word_to_index(vocab)
    
    for sentence in data:
        temp = CountVectorizer()
    
        temp_data = temp.fit([sentence])
        temp_vocab = temp_data.vocabulary_
        vector = np.zeros(len(vocab))
        
        for word, freq in temp_vocab.items():
            # we add 1 in freq as vocabulary didn't include word itself when counting the occurences 
            if freq+1 == 1:
                vector[word_to_in[word]] = 0
            elif freq+1 > 1 and freq <= 5:
                vector[word_to_in[word]] = 1
            else:
                vector[word_to_in[word]] = 2
            
        
        matrix.append(vector)
        print(vector)

def log_term_frq(data):
    vectorizer = CountVectorizer()
    x_train = vectorizer.fit(data)
    vocab = x_train.vocabulary_
    
    # check the frq in each row
    # divide by the max freq
    matrix = []
    word_to_in =  word_to_index(vocab)
    
    for sentence in data:
        temp = CountVectorizer()
    
        temp_data = temp.fit([sentence])
        temp_vocab = temp_data.vocabulary_
        vector = np.zeros(len(vocab))
        
        for word, freq in temp_vocab.items():
            # we add 1 in freq as vocabulary didn't include word itself when counting the occurences 
            freq = (freq + 1/len(data))
            freq = math.log10(freq) + 1
            vector[word_to_in[word]] = freq
        
        matrix.append(vector)
        print(vector)
                 
def binary_freq(data):
    #print("binary frequency")
    vectorizer = CountVectorizer()
    x_train = vectorizer.fit(data)
    vocab = x_train.vocabulary_
    
    matrix = []
    word_to_ind = word_to_index(vocab)
    
    for sentence in data:
        vector = np.zeros(len(word_to_ind))
        for word in sentence.split():
            if word in word_to_ind:
                vector[word_to_ind[word]] = 1
        matrix.append(vector)   
    
    print(matrix)
                
    #sp_sparse.vstack([sp_sparse.csr_matrix(my_bag_of_words(text, WORDS_TO_INDEX, DICT_SIZE))
    # now converting into
    
def frequency_based(data):
    vectorizer = CountVectorizer()
    x_train = vectorizer.fit_transform(data)
    print(x_train.toarray())

frequency_based(train[:4])
binary_freq(train[:4])
log_term_frq(train[:4])
caped_frq(train[:4])
lower_bound_frq(train[:4])