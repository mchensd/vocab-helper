#! python3
# Scraping NYT articles for a specific vocabulary word, returning the full sentence if found.

import json
from nytimesarticle import articleAPI
api = articleAPI('417fe849ada646a28b95d6185b70777c')
articles = api.search(q = 'precocious', begin_date = '20050101')
url = 'https://api.nytimes.com/svc/search/v2/'

# TODO
# Get more articles from earlier dates, make sure to get only articles not movies
# Option for user to get another sentence
# How to search for certain word (re?)

