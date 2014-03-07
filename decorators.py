#-------------------------------------------------------------------------------
# Name:        decorators
# Purpose:
#
# Author:      egrimm
#
# Created:     17/01/2014
# Copyright:   (c) egrimm 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import logging
from google.appengine.api import users
from config import config
from basehandler import BaseHandler
import socket
from urlparse import urlparse



def admin_required(handler):
    def check_session(self, *args, **kwargs):
        if users.get_current_user() is None:
            self.redirect(self.uri_for('home'), abort=True)
        elif users.is_current_user_admin() == False:
            self.redirect(self.uri_for('home'), abort=True)
        return handler(self, *args, **kwargs)
    return check_session


def user_required(handler):
    def check_session(self, *args, **kwargs):
        if users.get_current_user() is None:
            self.redirect(login_url, abort=True)
        elif self.session.get('is_rn_admin') == True:
            return self.redirect(self.uri_for('home'), abort=True)
        return handler(self, *args, **kwargs)
    return check_session