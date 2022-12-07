# twitter_webscrape.py

import configparser 
import tweepy as tw
import pandas as pd
import time as time
import json
import requests
from datetime import datetime, timedelta

def main(uname : str, count : int, tweet_df, user_df):
    config = configparser.RawConfigParser()
    config.read(filenames = 'twitter_keys.txt')
    accessToken = config.get('twitter','accessToken') 
    accessTokenSecret = config.get('twitter','accessTokenSecret') 
    bearerToken = config.get('twitter', 'bearerToken')

    client = tw.Client(bearerToken,accessToken,accessTokenSecret,wait_on_rate_limit=True)
    authorization = {"Authorization": "Bearer {}".format(bearerToken)}

    try:

        tweetJSON = scrape_tweets(client, authorization, uname, count)
        
        for i in range(count):
            if 'data' not in tweetJSON:
                break
            if i > (len(tweetJSON['data']) -1):
                break
            tweetData = json.dumps(tweetJSON['data'][i])
            tweetObj = json.loads(tweetData)
            

            try:
                get_obj = pd.json_normalize(tweetObj, ["entities", "urls"], ["id", "author_id", "text", "created_at"],errors="ignore")      
                
                metrics = pd.DataFrame(tweetObj['public_metrics'], index=[0])
                get_obj = pd.concat([get_obj, metrics], axis=1)
                reference = pd.DataFrame(tweetObj['referenced_tweets'])
                reference = reference.rename(columns={'type' : 'reference_type', 'id' : 'reference_id'})
                get_obj = pd.concat([get_obj, reference], axis=1)

            except BaseException:

                try:
                    get_obj = pd.json_normalize(tweetObj, ["entities", "urls"], ["id", "author_id", "text", "created_at"], 
                                                        errors="ignore") 
                    metrics = pd.DataFrame(tweetObj['public_metrics'], index=[0])
                    get_obj = pd.concat([get_obj, metrics], axis=1)

                except BaseException:

                    try:

                        get_obj = pd.json_normalize(tweetObj,errors="ignore") 
                        get_obj = get_obj[["id", "author_id", "text", "created_at"]].copy() 
                        metrics = pd.DataFrame(tweetObj['public_metrics'], index=[0])
                        get_obj = pd.concat([get_obj, metrics], axis=1)
                        reference = pd.DataFrame(tweetObj['referenced_tweets'])
                        reference = reference.rename(columns={'type' : 'reference_type', 'id' : 'reference_id'})
                        get_obj = pd.concat([get_obj, reference], axis=1)

                    except BaseException:

                        try:
                            get_obj = pd.json_normalize(tweetObj,errors="ignore") 
                            get_obj = get_obj[["id", "author_id", "text", "created_at"]].copy() 
                            metrics = pd.DataFrame(tweetObj['public_metrics'], index=[0])
                            get_obj = pd.concat([get_obj, metrics], axis=1)   

                        except BaseException as e:
                            print('failed on_status,',str(e))
                            time.sleep(3)

            tweet_df = tweet_df.append(get_obj, ignore_index=True)
  
        


        # ----------------------------
        #  Tweet JSON String Example
        # ----------------------------

        # {"public_metrics": {"retweet_count": 0, "reply_count": 0, "like_count": 0, "quote_count": 0}, 
        # "created_at": "2022-12-05T01:36:16.000Z", 
        # "entities": {"urls": [{"start": 123, "end": 146, "url": "https://t.co/rbVMJLNo90", "expanded_url": "https://youtu.be/TG9IjsxAWUs", 
        # "display_url": "youtu.be/TG9IjsxAWUs", "images": [{"url": "https://pbs.twimg.com/news_img/1598676629408346112/DM4NunjM?format=jpg&name=orig", 
        # "width": 1280, "height": 720}, 
        # {"url": "https://pbs.twimg.com/news_img/1598676629408346112/DM4NunjM?format=jpg&name=150x150", "width": 150, "height": 150}], 
        # "status": 200, "title": "\u306a\u304d\u305d - \u3052\u306e\u3052 feat.\u30ed\u30b9", 
        # "description": "\u25a1Streaming / Downloadhttps://orcd.co/genoge\u306a\u304d\u305d\u3068\u7533\u3057\u307e\u3059\u3002\u79c1\u3054\u3068\u304d\u3067\u5145\u5206\u3060\u304b\u3089\u25a0\u97f3\u697d\uff1a\u306a\u304d\u305d\u3000https://twitter.com/7kiso_nakiso\u25a0\u6b4c\u5531\uff1a\u30ed\u30b9\u3000https://twitter.com/ROSU7373\u25a0\u7d75\uff1a\u7f8a\u6b6f\u3000https://twitte...", 
        # "unwound_url": "https://www.youtube.com/watch?v=TG9IjsxAWUs&feature=youtu.be"}]}, "edit_history_tweet_ids": ["1234567890"], 
        # "text": "Example text:\n\nhttps://t.co/rbVMJLNo90", 
        # "author_id": "1234567890", "id": "1234567890"}

        userJSON = scrape_users(client, authorization, uname)
        userData = json.dumps(userJSON['data'])
        user_obj = pd.json_normalize(json.loads(userData))
        user_obj = user_obj.rename(columns={'public_metrics.followers_count' : 'followers_count', 'public_metrics.following_count' : 'following_count',
                                           'public_metrics.tweet_count' : 'tweet_count', 'public_metrics.listed_count' : 'listed_count'})
        user_df = user_df.append(user_obj, ignore_index=True)
        

        # ----------------------------
        #   User JSON String Example
        # ----------------------------

        # {"data": {"public_metrics": {"followers_count": 234, "following_count": 167, 
        # "tweet_count": 37094, "listed_count": 9}, "username": "username123", 
        # "id": "1234567890", "name": "John Doe"}}
        return tweet_df, user_df

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)


        



# ------------------------------------------------- #
#                helper functions                   #
# ------------------------------------------------- #

# finds count num of tweets by user (specified by username)
def scrape_tweets(client, authorization, uname : str, count : int):
    try:
        user = client.get_user(username=uname)
        dtformat = '%Y-%m-%dT%H:%M:%SZ'

        time = datetime.utcnow()
        start_time = time - timedelta(days=7)
        end_time = time - timedelta(seconds=15)
        start_time, end_time = start_time.strftime(dtformat), end_time.strftime(dtformat)

        search_tweets = f"https://api.twitter.com/2/users/{user.data.id}/tweets"
        tweet_params = {'max_results': count,'tweet.fields': 'id,author_id,created_at,text,public_metrics,entities,referenced_tweets','start_time': start_time, 'end_time': end_time}
        tweet_rules = {"add" : {"value" : "has:links"}}

        tweets = requests.request("GET", search_tweets, headers=authorization, params=tweet_params, json=tweet_rules)
        return tweets.json()

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)

# finds user's uID, display name, @username, and follower/following/tweet/listed count (specified by username)
def scrape_users(client, authorization, uname : str):
    try:
        user = client.get_user(username=uname)

        search_user = f"https://api.twitter.com/2/users/{user.data.id}"
        user_params = {'user.fields': 'id,name,username,public_metrics'}



        userInfo = requests.request("GET", search_user, headers=authorization, params=user_params)
        return userInfo.json()

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)



def scrape_author_tweets():
    articles_df = pd.read_csv('articles_raw_w_twt.csv')
    author_twts = articles_df['twitter'].tolist()
    nonnull_twts = [x for x in author_twts if pd.isnull(x) == False and x != 'nan']
    distinct_author_twts = []
    [distinct_author_twts.append(x) for x in nonnull_twts if x not in distinct_author_twts]
    

    tweet_df = pd.DataFrame(columns=['start', 'end', 'url', 'expanded_url', 'display_url', 'images', 
                                            'status', 'title', 'description', 'unwound_url', 'id', 'author_id', 
                                            'text', 'created_at', 'retweet_count', 'reply_count',
                                            'like_count', 'quote_count', 'reference_type', 'reference_id'])

    user_df = pd.DataFrame(columns=['name', 'username', 'id', 'followers_count', 'following_count', 'tweet_count', 
                                        'listed_count'])
    try:
        for i in range(len(distinct_author_twts)):
            tweet_df, user_df = main(distinct_author_twts[i], 5, tweet_df, user_df)
            
        tweet_df.to_csv("tweetData.csv")
        user_df.to_csv("userData.csv")

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)

scrape_author_tweets()