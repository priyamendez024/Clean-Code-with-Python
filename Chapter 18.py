# Chapter 18: Building a Clean REST API with Flask

from flask import Flask, jsonify, request, Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app