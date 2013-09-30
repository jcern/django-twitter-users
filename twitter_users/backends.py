from mongoengine import *
from twitter_users.models import *

from django.utils.encoding import smart_str
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.hashers import check_password, make_password
from django.utils.translation import ugettext_lazy as _

import datetime

REDIRECT_FIELD_NAME = 'next'

class TwitterBackend(object):
    """Authenticate using MongoEngine and mongoengine.django.auth.User.
    """

    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        user = User.objects(username=username).first()
        if user:
            return user
        return None

    def get_user(self, user_id):
        return User.objects.with_id(user_id)


def get_user(userid):
    """Returns a User object from an id (User.id). Django's equivalent takes
    request, but taking an id instead leaves it up to the developer to store
    the id in any way they want (session, signed cookie, etc.)
    """
    if not userid:
        return AnonymousUser()
    return TwitterBackend().get_user(userid) or AnonymousUser()
