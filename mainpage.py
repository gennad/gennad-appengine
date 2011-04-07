# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from models import Quote
from random import choice
from google.appengine.ext import db

class MainPage(webapp.RequestHandler):
  def get(self):
    quotes = Quote.all()
    quotes_list = []
    if not quotes.count():
        quote = Quote(content=u"Приветик Кош!")
        db.put(quote)
        quotes = Quote.all()

    for q in quotes:
        quotes_list.append(q)

    quote = choice(quotes_list)

    template_values = {
        'quote': quote.content
    }

    path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
