#!/usr/bin/env python

'''
Created on Jul 15, 2012

@author: shahr
'''

from google.appengine.ext import db

class Location(db.Model):
    email = db.StringProperty()
    lat = db.StringProperty()
    long = db.StringProperty()
    datetime = db.DateTimeProperty(auto_now_add = True)

    @staticmethod
    def location_key(email):
        return db.Key.from_path("Location", email or "default")




        