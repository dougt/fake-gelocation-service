
import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({"location": { "lat": 37.4133, "lng": -122.081, "accurancy": 42}}))

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("fake geolocation testing service")

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)

