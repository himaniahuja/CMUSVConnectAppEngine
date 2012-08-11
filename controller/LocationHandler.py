from google.appengine.ext import db
from google.appengine.ext import webapp
from model.Location import Location

import urllib
import json

class LocationHandler(webapp.RequestHandler):
    def get(self):
        email = self.request.get('email')
        limit = self.request.get('limit')
        query = ""
        if len(limit) > 0 and int(limit) > 0: 
            query = "select * from Location where ANCESTOR IS :1 order by datetime desc limit %s" % limit
        else : 
            query = "select * from Location where ANCESTOR IS :1 order by datetime desc "
        
        locations = db.GqlQuery(query, Location.location_key(email))
        
        retObject = []
        for location in locations:
            record = {} 
            record['email'] = location.email
            record['lat'] = location.lat
            record['long'] = location.long
            record['DateTime'] = str(location.datetime)
            retObject.append(record)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retObject))
            
    def post(self):
        self.response.out.write(self.request)
        lat = self.request.get('lat')
        long = self.request.get('long')
        email = self.request.get('email')
        
        location = Location(parent=Location.location_key(email))
        self.response.out.write("location : %s" %location)
        location.lat = lat
        location.long = long
        location.email = email
        location.put()
        self.redirect('/LocSubmit?' + urllib.urlencode({'email' : email}))