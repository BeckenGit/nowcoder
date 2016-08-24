#!/usr/bin/python
#-*- coding: utf-8 -*-


import itertools
from collections import Counter
import numpy as np
import re, os
import csv
max_len = 200
def clean_str(string):
    string = unicode(string, 'utf-8')
    string = re.sub(ur"[0-9a-zA-Z～@+*\s]", "", string)
    string = re.sub(ur"[：；，、×.“”…_【】（）():,\#《》〈丶&\-\[\]\/]", "", string)
    string = re.sub(ur"[。！？]", "", string)
    return string[0: max_len]

path = "/data/traindata.csv"
with open(os.getcwd() + path, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    texts = [[clean_str(row[1]), row[2]] for row in spamreader]
    sentences = [text[0] for text in texts]

def get_vocabulary():
    char_dict = dict()
    for sentence in sentences:
        for cn_char in sentence:
            if cn_char not in char_dict:
                char_dict[cn_char] = len(char_dict) + 1
    return char_dict

def get_labels_list():
    classifies_set = set()
    for text in texts:
        classifies_set.add(text[1])
    return list(classifies_set)

def load_data_and_labels():
    sentences_digital = []
    char_dict = get_vocabulary()
    for sentence in sentences:
        sentence_digital = np.zeros(max_len)
        for i, cn_char in enumerate(sentence):
            sentence_digital[i] = char_dict[cn_char]
        sentences_digital.append(sentence_digital)

    classifies_list = get_labels_list()
    classifies_size = len(classifies_list)
    labels_dicts = dict()
    for i, classify in enumerate(classifies_list):
        classify_label = np.zeros(classifies_size)
        classify_label[i] = 1
        labels_dicts[classify] = classify_label
    for label in labels_dicts:
        print label, labels_dicts[label]
    labels = [labels_dicts[text[1]] for text in texts]
    return [np.array(sentences_digital), np.array(labels)]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int(len(data)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
