from flask import Flask, request
from flask_restful import Api, Resource
from auth import Authentication

app = Flask(__name__)
api = Api(app)

class login(Resource):
    def post(self):
        auth = request.authorization
        return Authentication.login(auth)

class lteOcsProv(Resource):
    def post(self):
        data = request.get_json()
        auth = request.authorization
        return register_merchant(data, auth)

api.add_resource(login, '/sltdevops/apiServices/token')

api.add_resource(lteOcsProv, '/sltdevops/apiServices/lte')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22500)
