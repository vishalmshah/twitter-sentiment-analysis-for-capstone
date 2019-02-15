

# There is no need for this file
# I found 1.6 million tweets from kaggle
# https://www.kaggle.com/kazanova/sentiment140 






#---------------------------------------------------------


# This is where we use the twitter api to get data
# Let's use like 5000 random tweets to train
# We will put all of the tweets in a pandas dataframe and export it to a pickle (.pkl) file
# This data will go into the raw directory

######> This is useful for production stuff, but kaggle has twitter data
###### 1.6 million tweets are in the dataset
###### https://www.kaggle.com/kazanova/sentiment140 

# # READ THIS: none of this works just run these commands in the terminal
# # pip install twitterscraper
# # twitterscraper "*" -c -l=5000 --output=raw.csv -bd 2015-01-01 ed 2018-12-31 --lang=en



# import pandas as pd
# from twitterscraper import query_tweets
# import pprint as pprint
# import subprocess
# import codecs, json


# if __name__ == '__main__':

#   subprocess.call(['twitterscraper "*" -c -l=5000 --output=raw.csv -bd 2015-01-01 ed 2018-12-31 --lang=en'])


#   with codecs.open('tweets.json', 'r', 'utf-8') as f:
#       tweets = json.load(f, encoding='utf-8')

#   list_tweets = [list(elem.values()) for elem in tweets]
#   list_columns = list(tweets[0].keys())
#   df = pd.DataFrame(list_tweets, columns=list_columns)

#   df.to_pickle('pickled_tweets.pkl')
#   df.to_csv('comma_sep_tweets.csv')
