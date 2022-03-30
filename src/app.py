from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client  = MongoClient('MongoDB',27017)
print("connected to mongoDB sucessfully")

@app.route('/')
def hello_world():
    return "hello world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)