from google.appengine.ext import db
from google.appengine.ext import webapp
from model.Message import Message

import urllib
import json

class MessageHandler(webapp.RequestHandler):
    def get(self):
        email = self.request.get('email')
        limit = self.request.get('limit')
        query = ""
        messages = []
        if len(email) > 0 :
            if len(limit) > 0 and int(limit) > 0: 
                query = "select * from Message where ANCESTOR IS :1 order by datetime desc limit %s" % limit
            else : 
                query = "select * from Message where ANCESTOR IS :1 order by datetime desc "
            messages = db.GqlQuery(query, Message.message_key(email))
        else : 
            if len(limit) > 0 and int(limit) > 0: 
                query = "select * from Message order by datetime desc limit %s" % limit
            else : 
                query = "select * from Message order by datetime desc limit 50" 
            messages = db.GqlQuery(query)
       
        retObject = []
        for message in messages:
            record = {} 
            record['email'] = message.email
            record['text'] = message.text
            record['DateTime'] = str(message.datetime)
            retObject.append(record)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retObject))
        
    def post(self):
        self.response.out.write(self.request)
        text = self.request.get('text')
        email = self.request.get('email')
        
        message = Message(parent=Message.message_key(email))
        self.response.out.write("message : %s" %message)
        message.text = text
        message.email = email
        message.put()
        self.redirect('/MessageSubmit?' + urllib.urlencode({'email' : email}))