from google.appengine.ext import db

class Subscriber(db.Model):
    email = db.EmailProperty()
    name = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
