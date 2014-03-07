# -*- coding: utf-8 -*-
import logging
import sys

# related third party imports
import webapp2
from google.appengine.api import users # we are using this for authentication
from google.appengine.ext import ndb

# local application/library specific imports
import models # we are using this for authorization and storing of further pii
from basehandler import BaseHandler
from decorators import user_required, admin_required
from config import config


class MainHandler(BaseHandler):

    def get(self):
        params = {}
        return self.render_template('home.html', **params)