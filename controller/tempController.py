from flask import Flask, request
import flask_cors

import util.CmmUtil as cu
import service.tempService as ta

application = Flask(__name__)

flask_cors.CORS(application)

@application.route("/temp")
def tempList():

    return {"temp": ta.tempService.getTemp()}


if __name__ == "__main__":
    application.run(host="127.0.0.1", port=3800)
