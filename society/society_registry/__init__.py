import markdown
import os

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

#import firebase libs
import firebase_admin
from firebase_admin import credentials, db

# Initialize firebase admin
cred = credentials.Certificate('recsoi-firebase-adminsdk-sjua3-c065716785.json')
# cred = credentials.
# Authonticate using user pass
# email = input("email: /n")
# password = input("password: /n")


default_app  = firebase_admin.initialize_app(cred,{'databaseURL' : 'https://recsoi.firebaseio.com/'})


# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

#initalize databse for firebase
root = db.reference()


#Initalize first route for project documentation
@app.route("/")
def index():
    """Present some documentation"""
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)

class society(Resource):
    def get(self):
        ref = root.child('society')
        result = ref.get()
        #societies = []

        #for key in result:
        #    societies.append(result[name])

        return {'message': 'Success', 'data': result}, 200

    def post(self):
        ref = root.child('society')
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('address', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        ref.push(args)

        return {'message': 'Society registered', 'data': args}, 201    


class test(Resource):
    def get(self):
        check = root.child('society').get()
    #     new_user = root.child('society').push({
    # 'name' : 'Krishna Vihar', 
    # 'address' : 'Plot-109, Krishna Vihar, Ghansoli'
    #                                         })
        return check

api.add_resource(test, '/get_news')
api.add_resource(society, '/society')