from flask import Flask, jsonify, request, redirect, render_template, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import json
from urldata import *
from jsonUtils import *

app = Flask(__name__)
CORS(app)
api = Api(app)

class home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("index.html"), 200, headers)

class shorten(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return pageNotFound()

        link = data.get('url')
        alias = data.get('alias')
        ob = urldata()
        ob.originalURL = link

        if not link:
            return pageNotFound()

        if not ob.validate(link):
            return responseInvalidURL(ob)
        if alias:
            if not ob.validateAlias(alias):
                return responseInvalidAlias(ob)
            if ob.checkAlias(alias):
                ob.shortenWithAlias(link, alias)
                return responseOk(ob)
            else:
                return responseAliasTaken(ob)

        ob.shorten(link)
        return responseOk(ob)

class redirectTo(Resource):
    def get(self, alias):
        ob = urldata()
        ob.getURL(alias)
        if not ob.originalURL:
            return pageNotFound()
        else:
            return redirect(ob.originalURL)
        

api.add_resource(home, '/')
api.add_resource(shorten, '/shorten')
api.add_resource(redirectTo, '/<string:alias>')

if __name__ == '__main__':
    app.run(debug=True)
