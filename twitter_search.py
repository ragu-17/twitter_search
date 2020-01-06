from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['keyword1', 'keyword2']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see english tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'aaaaaa',
        consumer_secret = 'bbbbb',
        access_token = 'cccc-dddd',
        access_token_secret = 'eeee'
     )
     
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
