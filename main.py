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

# wmata api web app

import webapp2
from google.appengine.ext import ndb
import cgi
import jinja2
import os
import urllib2
import json
from trains import *



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        allTrains = dbdata().get_trains()   
        B=station('Ballston-MU',allTrains)
        T=station('Tysons Corner',allTrains)
    
        Ballston=[train for train in B.get_trains() if train.get_dest()=='Wiehle']
        Tysons= [train for train in T.get_trains() if train.get_dest()=='Largo']   
        
        
        template_values={'Ballston':Ballston, 'Tysons':Tysons}
        template = JINJA_ENVIRONMENT.get_template('./templates/layout.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
