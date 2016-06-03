
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "P92NtY2qIdxUfjsGfivEijmsr"
csecret = "NBHSV0I3RbocI4hBgI3sZPWTTOfty0riJEqi54wC2Fk301R7Wv"
atoken = "738207948867014656-u8qyopbKISQcFrUFskwSKoyaE6eL0b1"
asecret = "IlB2dUi9ViIaRr8tFgBtq7SWDTSLTAdUkgFsDqVsKiBv7"
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
    db = server.create('tweets2')
except:
    db = server['tweets2']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-78.501928,-0.119691,-78.472101,-0.091281])  #condado/ponciano