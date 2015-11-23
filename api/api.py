from eve import Eve
from flask.ext.cors import CORS
import json
from flask import request
from pymongo import MongoClient
import os

app = Eve()
cors = CORS(app)


@app.route("/version")
def version():
    return 'Deep API v0.0.2'


@app.route("/_status/healthcheck")
def healthcheck():
    return 'Deep is healthy'


@app.route("/_status/healthcheck/db")
def healthcheck_db():
    mongo_host = os.environ.get('MONGO_SERVICE_HOST')
    mongo_port = os.environ.get('MONGO_SERVICE_PORT')
    mongo_url = 'mongodb://' + mongo_host + ":" + mongo_port + '/'
    client = MongoClient(mongo_url)
    db = client.deep

    return "Healthy: " + str(db.name)


@app.route("/debug", methods=['POST'])
def add_link():
    pjson = json.loads(request.data)
    app.logger.debug(pjson)
    return request.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
