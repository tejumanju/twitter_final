 import tweepy
import os # operating system library

def create_api():
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET ')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    
        api.verify_credentials()
  
        
    print('API created')
    return api

#complete code
import time
def emoji_follower_count(user):
    emoji_numbers = {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                     4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

    uf_split = [int(i) for i in str(user.followers_count)]

    emoji_followers = ''.join([emoji_numbers[k]
                               for k in follower_count_list if k in emoji_numbers.keys()])

    return emoji_followers 

    api = create_api()

    while True:
        
        user = api.get_user('the_ameen_manna')

        api.update_profile(name=f'aMEEr|{emoji_follower_count(user)} Followers')
        print(f'Updating twitter profile: {emoji_follower_count(user)}')
        print("Waiting to refresh..")
        time.sleep(60)


main()
