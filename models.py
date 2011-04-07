from google.appengine.ext import db

class Quote(db.Model):
    content = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    date_heard = db.DateTimeProperty()
