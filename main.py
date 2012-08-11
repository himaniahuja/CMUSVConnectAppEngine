#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import datetime
import urllib
import json

from google.appengine.ext import webapp
from google.appengine.api import users
from controller.LocationSubmitHandler import LocationSubmitHandler
from controller.LocationHandler import LocationHandler
from controller.MessageSubmitHandler import MessageSubmitHandler
from controller.MessageHandler import MessageHandler

VERSION = 1.0


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(VERSION)

class PeopleHandler(webapp.RequestHandler):
    def get(self):
	f = open("data/People.json", 'r')
	
	self.response.out.write(f.read())

app = webapp.WSGIApplication([('/', MainHandler), 
				('/People.json', PeopleHandler),
                ('/LocSubmit', LocationSubmitHandler),
                ('/Location.json', LocationHandler),
                ('/Location_Post', LocationHandler),
                ('/MessageSubmit', MessageSubmitHandler),
                ('/Message.json', MessageHandler),
                ('/Message_Post', MessageHandler),
                ('/Version', MainHandler),
                ('/Version', MainHandler),
                ],
                              debug=True)
