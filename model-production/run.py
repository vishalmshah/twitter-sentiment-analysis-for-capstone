# This is where we will manipulate the data
# We will put the result of this into the model
# This will go in a pickle (.pkl) file that goes in the data directory

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sentlex
import sentlex.sentanalysis
from textblob import TextBlob, Word
from sklearn.feature_extraction.text import CountVectorizer
import jamspell
import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import datetime
import sys

# This is from VADER sentiment analyzer
# https://github.com/cjhutto/vaderSentiment
def vader_scores(series):
  # print("start vader_scores" + str(datetime.now()))
  analyser = SentimentIntensityAnalyzer()
  scores = []
  for sentence in series:
    scores.append(analyser.polarity_scores(sentence))
  vader = pd.DataFrame(scores)
  # print("end vader_scores" + str(datetime.now()))
  return vader

# This is for the sentlex sentiment lexicon
# https://github.com/bohana/sentlex
def sentlex_scores(series):
  # print("start sentlex_scores" + str(datetime.now()))
  SWN = sentlex.SWN3Lexicon()
  classifier = sentlex.sentanalysis.BasicDocSentiScore()
  document = []
  for sentence in series:
    document.append(list(classifier.classify_document(sentence, tagged=False, L=SWN, a=True, v=True, n=False, r=False, negation=True, verbose=False)))
  # print("end sentlex_scores" + str(datetime.now()))
  return pd.DataFrame(document)

# A couple things to make it easier for the algo to notice patterns
# https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
def text_cleaning(df):
  # print("start text_cleaning" + str(datetime.now()))
  # Spelling Correction
  corrector = jamspell.TSpellCorrector()
  corrector.LoadLangModel('./en.bin')
  df['Text'] = df['Text'].map(lambda x: corrector.FixFragment(x))
  # print("end spelling" + str(datetime.now()))
  # Lemmatization
  df['Text'] = df['Text'].map(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
  # print('lemma')
  # print("end lemma" + str(datetime.now()))
  # # Bag of Words
  # bow = CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1),analyzer = "word")
  # df['Bag_of_Words'] = bow.fit_transform(df['Text'])
  # # print('bow')
  # print("end bow" + str(datetime.now()))
  # Sci Kit Learn Sentiment
  df['SKL_Sentiment'] = df['Text'].map(lambda x: TextBlob(x).sentiment[0])
  # print('skl')
  # print("end text_cleaning" + str(datetime.now()))
  return df



# ----------------------

# print('running python')
# print(sys.argv[1])

# For running on single sentence
data = pd.DataFrame(data = {'Text': [sys.argv[1]]})
# print(data)

data = text_cleaning(data)

vader_df = vader_scores(data['Text'])
data['Vader_Neg'] = vader_df['neg']
data['Vader_Neu'] = vader_df['neu']
data['Vader_Pos'] = vader_df['pos']
data['Vader_Compound'] = vader_df['compound']

sentlex_df = sentlex_scores(data['Text'])
data['Sentlex_Pos'] = sentlex_df[0]
data['Sentlex_Neg'] = sentlex_df[1]

data = data.drop('Text', axis=1)

# print(data)

# Running the model on new data
model = tf.keras.models.load_model('../../model-development/model/twitter_sentiment.model')
predictions = model.predict([data.values])

print(predictions[0][1])
# print(np.argmax(predictions[0]))

sys.stdout.flush()
# data.to_csv('./model-development/data/jflsdkjflsdkjf.csv')
# data.to_pickle('./model-development/data/testing_data.csv')

