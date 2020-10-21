from flask import Flask, request
import flask_cors

import util.CmmUtil as cu
import service.WeatherService as ta
import service.tempService as te

application = Flask(__name__)

flask_cors.CORS(application)

@application.route("/weather")
def weatherlist():

    return {"weather": ta.WeatherService.getWeather()}


@application.route("/temp")
def tempList():

    return {"temp": te.tempService.getTemp()}


if __name__ == "__main__":
    application.run(host="127.0.0.1", port=3600)
