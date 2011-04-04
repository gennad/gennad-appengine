from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from models import Subscriber
from google.appengine.ext import db
import simplejson as json

class Subscribe(webapp.RequestHandler):
    def get(self):

        template_values = {
         }

        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        email = self.request.get('email')
        name = self.request.get('name')
        subscriber = Subscriber(email=email, name=name)
        db.put(subscriber)

        response = {'result': True}
        dumped = json.dumps(response)
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
        self.response.out.write(dumped)

application = webapp.WSGIApplication(
                                     [('/subscribe', Subscribe),
                                      ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
