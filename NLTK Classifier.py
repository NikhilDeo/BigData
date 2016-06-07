# -*- coding: utf-8 -*-
"""
Nikhil Deo
Based on instructions from Emma Anderson whose instructions were based on instrutions from Laurent Luce
"""

import re
import nltk

stopfile = open("stopwords.txt")
csvfile = open("training_neatfile2.csv", "r", errors = "ignore")

tweets = []
labels = []
stopwords = []
split_tweets = []

for line in csvfile:
    line = line.split(",")
    labels.append(line[0])
    tweets.append(line[1])
    
for ii in stopfile:
    ii = ii.replace("\n", "")
    stopwords.append(ii)
    
for t in range(len(tweets)):    
    letters_only = re.sub("[^a-zA-Z]", "", tweets[t])
    letters_only = letters_only.lower()
    words = letters_only.split()
    words = [w for w in words if not w in stopwords]
    if not labels[t] == 1:
        split_tweets.append((words, labels[t]))
        
#Make a list of all the words in the training set
def get_words_in_tweets(tweets):
    all_words = []
    for (words, label) in tweets:
        all_words.extend(words)
    return all_words
    
#Get the frequencies of those words
def get_word_features(wordList):
    freq = nltk.FreqDist(wordList)
    word_features = freq.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' %word] = word in document_words
    return features
    
def tokenize(tweet):
    letters_only = re.sub("[^a-zA-Z]", "", tweet)
    letters_only = letters_only.lower()
    words = letters_only.split()
    words = [w for w in words if not w in stopwords]
    return words
    
all_words = get_words_in_tweets(split_tweets)
word_features = get_word_features(all_words)

training_set = nltk.classify.apply_features(extract_features, split_tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

dataBallard = open("tweetDataBallardHS.txt", "r", errors = 'ignore')
classBallard = []
dataBellevue = open("tweetDataBellevueHS.txt", "r", errors = 'ignore')
classBellevue = []
dataFranklin = open("tweetDataFranklinHS.txt", "r", errors = 'ignore')
classFranklin = []
dataUPrep = open("tweetDataUPA.txt", "r", errors = 'ignore')
classUPrep = []
dataWestSeattle = open("tweetDataWSHS.txt", "r", errors = 'ignore')
classWestSeattle = []

for x in dataBallard:
    try:
        x = x.split(',')
        classBallard.append(classifier.classify(extract_features(tokenize(x[1]))))
    except IndexError:
        pass
for x in dataBellevue:
    try:    
        x = x.split(',')
        classBellevue.append(classifier.classify(extract_features(tokenize(x[1]))))
    except IndexError:
        pass
for x in dataFranklin:
    try:    
        x = x.split(',')
        classFranklin.append(classifier.classify(extract_features(tokenize(x[1]))))
    except IndexError:
        pass
for x in dataUPrep:
    try:    
        x = x.split(',')
        classUPrep.append(classifier.classify(extract_features(tokenize(x[1]))))
    except IndexError:
        pass
for x in dataWestSeattle:
    try:    
        x = x.split(',')
        classWestSeattle.append(classifier.classify(extract_features(tokenize(x[1]))))
    except IndexError:
        pass
    
allClassifiedData = {}
allClassifiedData["classBallard"] = classBallard
allClassifiedData["classBellevue"] = classBellevue
allClassifiedData["classFranklin"] = classFranklin
allClassifiedData["classUPrep"] = classUPrep
allClassifiedData["classWestSeattle"] = classWestSeattle

happinessDict = {}
for x in allClassifiedData:
    counterP = 0
    counterN = 0
    for z in range(len(allClassifiedData[x])):
        if allClassifiedData[x][z] == '4':
            counterP = counterP+1
        elif allClassifiedData[x][z] == '-2':
            counterN = counterN+1
    happinessDict[x] = ((counterP/len(allClassifiedData[x])), (counterN/len(allClassifiedData[x])))