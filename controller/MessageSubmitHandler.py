from google.appengine.ext import db
from google.appengine.ext import webapp
from model.Message import Message


class MessageSubmitHandler(webapp.RequestHandler):
    def get(self):
        email = self.request.get('email')
        messages = db.GqlQuery(
                               "select * from Message where ANCESTOR IS :1 order by datetime desc limit 1 ", Message.message_key(email))
        
        for message in messages: 
            self.response.out.write('Existing value for : <b>email: %s, text: %s, timestamp: %s</b>' % (message.email, message.text, message.datetime))
        
        self.response.out.write("""<html>
        <body>
            <form action="/Message_Post" method="post">
            <div>
                <textarea name="text" rows="1" cols="20"></textarea>
                <textarea name="email" rows="1" cols="20"></textarea>   
            </div>
            <div>
                <input type="submit" value="set text / email">
            </div>
            </form>
            
            To get data in json: go to <a href="/Message.json">Message.json</a> and pass email as a parameter. eg /message.json?email=rohan.shah 
            </body></html>""")