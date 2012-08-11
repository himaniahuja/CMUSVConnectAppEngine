from google.appengine.ext import db
from google.appengine.ext import webapp
from model.Location import Location


class LocationSubmitHandler(webapp.RequestHandler):
    def get(self):
        email = self.request.get('email')
        locations = db.GqlQuery("select * from Location where ANCESTOR IS :1 order by datetime desc limit 1 ", Location.location_key(email))
        
        for location in locations: 
            self.response.out.write('Existing value for : <b>email: %s, lat: %s, long: %s, timestamp: %s</b>' % (location.email, location.lat, location.long, location.datetime))
        
        self.response.out.write("""<html>
        <body>
            <form action="/Location_Post" method="post">
            <div><textarea name="lat" rows="1" cols="20"></textarea>
            <textarea name="long" rows="1" cols="20"></textarea></div>
            <textarea name="email" rows="1" cols="20"></textarea>   
            <div><input type="submit" value="set lat/long"></div>
            </form>
            
            To get data in json: go to <a href="/Location.json">Location.json</a> and pass email as a parameter. eg /location.json?email=rohan.shah 
            </body></html>""")