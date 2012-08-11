
from google.appengine.ext import db

class Message(db.Model):
    email = db.StringProperty()
    text = db.StringProperty()
    datetime = db.DateTimeProperty(auto_now_add = True)      
    
    @staticmethod
    def message_key(email):
        return db.Key.from_path("Message", email or "default")
