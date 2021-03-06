from flask import Flask, jsonify, make_response, request, Response
from flask_jwt_extended import jwt_required, create_access_token, JWTManager
import json

# Generate the test payload
test_data = {
    'test': ['this', 'is', 'a', 'test']
}
# Create the login details
username = 'Client'
password = 'password'

# Initialise the application
app = Flask(__name__)
# Update the secret key 
app.config['SECRET_KEY'] = 'Client_key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(3600)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
JWTManager(app)

# Create the login route - this is a POST
@app.route('/login', methods=['POST'])
def login(request=request):
    (request.headers.get("authorization"))
    data = request.authorization
    if not data or not data.username or not data.password:
        return make_response('Could not verify your details'.format(data, data.username, data.password),
                             401,
                             {'WWW-authenticate': 'Login required'})

    user = username

    if not user:
        return make_response('Could not verify your details', 401,
                             {'WWW-authenticate': 'Login required'})
# Return a token if the login is successful
    if password == data.password:
        token = create_access_token(identity=data.username)
        return jsonify(token=token)
        
@app.route('/get_data', methods=['GET'])
@jwt_required()
def get(request=request):
    
    return jsonify(test_data)

if __name__ == '__main__':
    app.run(debug=True)
