# This is where we will manipulate the data
# We will put the result of this into the model
# This will go in a pickle (.pkl) file that goes in the data directory

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sentlex
import sentlex.sentanalysis
from textblob import TextBlob, Word
from sklearn.feature_extraction.text import CountVectorizer
import jamspell
import pandas as pd
from datetime import datetime

# This is from VADER sentiment analyzer
# https://github.com/cjhutto/vaderSentiment
def vader_scores(series):
  print("start vader_scores" + str(datetime.now()))
  analyser = SentimentIntensityAnalyzer()
  scores = []
  for sentence in series:
    scores.append(analyser.polarity_scores(sentence))
  vader = pd.DataFrame(scores)
  print("end vader_scores" + str(datetime.now()))
  return vader

# This is for the sentlex sentiment lexicon
# https://github.com/bohana/sentlex
def sentlex_scores(series):
  print("start sentlex_scores" + str(datetime.now()))
  SWN = sentlex.SWN3Lexicon()
  classifier = sentlex.sentanalysis.BasicDocSentiScore()
  document = []
  for sentence in series:
    document.append(list(classifier.classify_document(sentence, tagged=False, L=SWN, a=True, v=True, n=False, r=False, negation=True, verbose=False)))
  print("end sentlex_scores" + str(datetime.now()))
  return pd.DataFrame(document)

# A couple things to make it easier for the algo to notice patterns
# https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
def text_cleaning(df):
  print("start text_cleaning" + str(datetime.now()))
  # Spelling Correction
  corrector = jamspell.TSpellCorrector()
  corrector.LoadLangModel('./en.bin')
  df['Text'] = df['Text'].map(lambda x: corrector.FixFragment(x))
  print("end spelling" + str(datetime.now()))
  # Lemmatization
  df['Text'] = df['Text'].map(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
  # print('lemma')
  print("end lemma" + str(datetime.now()))
  # # Bag of Words
  # bow = CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1),analyzer = "word")
  # df['Bag_of_Words'] = bow.fit_transform(df['Text'])
  # # print('bow')
  # print("end bow" + str(datetime.now()))
  # Sci Kit Learn Sentiment
  df['SKL_Sentiment'] = df['Text'].map(lambda x: TextBlob(x).sentiment[0])
  # print('skl')
  print("end text_cleaning" + str(datetime.now()))
  return df



# ----------------------

# raw_data = pd.read_csv('./model-development/raw/training_raw_data.csv', encoding="ISO-8859-1", header=None, names=['Sentiment', 'ID', 'Date', 'Query', 'User', 'Text'])

# # Once for training data
# raw_data = pd.read_csv('./model-development/raw/train.csv', encoding="ISO-8859-1", names=['ItemID', 'Sentiment', 'Text'])

# final_data = pd.DataFrame()
# final_data['Text'] = raw_data['Text']
# final_data['Sentiment'] = raw_data['Sentiment']

# # final_data = text_cleaning(final_data.head(100))
# final_data = text_cleaning(final_data)

# # vader_df = vader_scores(raw_data['Text'].head(100))
# vader_df = vader_scores(raw_data['Text'])
# final_data['Vader_Neg'] = vader_df['neg']
# final_data['Vader_Neu'] = vader_df['neu']
# final_data['Vader_Pos'] = vader_df['pos']
# final_data['Vader_Compound'] = vader_df['compound']

# # sentlex_df = sentlex_scores(raw_data['Text'].head(100))
# sentlex_df = sentlex_scores(raw_data['Text'])
# final_data['Sentlex_Pos'] = sentlex_df[0]
# final_data['Sentlex_Neg'] = sentlex_df[1]

# final_data.to_csv('./model-development/data/training_data.csv')
# # final_data.to_pickle('./model-development/data/training_data.csv')


# # And again for testing data
# raw_data = pd.read_csv('./model-development/raw/test.csv', encoding="ISO-8859-1", names=['ItemID', 'Text'])

# final_data_test = pd.DataFrame()
# final_data_test['Text'] = raw_data['Text']

# # final_data_test = text_cleaning(final_data_test.head(100))
# final_data_test = text_cleaning(final_data_test)

# # vader_df = vader_scores(raw_data['Text'].head(100))
# vader_df = vader_scores(raw_data['Text'])
# final_data_test['Vader_Neg'] = vader_df['neg']
# final_data_test['Vader_Neu'] = vader_df['neu']
# final_data_test['Vader_Pos'] = vader_df['pos']
# final_data_test['Vader_Compound'] = vader_df['compound']

# # sentlex_df = sentlex_scores(raw_data['Text'].head(100))
# sentlex_df = sentlex_scores(raw_data['Text'])
# final_data_test['Sentlex_Pos'] = sentlex_df[0]
# final_data_test['Sentlex_Neg'] = sentlex_df[1]

# final_data_test.to_csv('./model-development/data/testing_data.csv')
# # final_data_test.to_pickle('./model-development/data/testing_data.csv')



# For 1.6 million if neccessary
raw_data = pd.read_csv('./model-development/raw/training_raw_data.csv', encoding="ISO-8859-1", header=None, names=['Sentiment', 'ID', 'Date', 'Query', 'User', 'Text'])

final_data = pd.DataFrame()
final_data['Text'] = raw_data['Text']
final_data['Sentiment'] = raw_data['Sentiment']

# final_data = text_cleaning(final_data.head(100))
final_data = text_cleaning(final_data)

# vader_df = vader_scores(raw_data['Text'].head(100))
vader_df = vader_scores(raw_data['Text'])
final_data['Vader_Neg'] = vader_df['neg']
final_data['Vader_Neu'] = vader_df['neu']
final_data['Vader_Pos'] = vader_df['pos']
final_data['Vader_Compound'] = vader_df['compound']

# sentlex_df = sentlex_scores(raw_data['Text'].head(100))
sentlex_df = sentlex_scores(raw_data['Text'])
final_data['Sentlex_Pos'] = sentlex_df[0]
final_data['Sentlex_Neg'] = sentlex_df[1]

final_data.to_csv('./model-development/data/testing_1600000_data.csv')
# final_data.to_pickle('./model-development/data/testing_data.csv')