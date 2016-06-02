
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "9EqJwQhPn6Wfl5vXoltDenIOD"
csecret = "BgKYrgYaQ1biNJbk8X7F68Y5OelSF8KSkIBADcncusYX9fShtT"
atoken = "735575706072145920-2FLMGFNFBY1Ucn4MS6A5mU8VMi8QSuI"
asecret = "kvdhWHAM0ZNV7IwRcxACrQ894juGX7cd4X7QNTyLdvWwv"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
    
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('tweet3')
except:
    db = server['tweet3']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-78.510361,-0.205993,-78.484783,-0.186081])  #Mariscal Sucre