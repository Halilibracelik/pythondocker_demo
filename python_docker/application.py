
import flask
from flask import request
import json, time
import requests


app = flask.Flask(__name__)




api_key = "5581ce99e223e0f0f440ddb95dcb1766"
base_url = "http://api.openweathermap.org/data/2.5/weather?"




@app.route('/') 

def index():
    name_surname = {'name': 'Halil Ibrahim', 'surname': 'CELIK'}
    
    return json.dumps(name_surname)


@app.route('/temperature', methods=['GET']) 

def temperature(): 
    
    city = request.args.get('city')

    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    current_temperature = y["temp"]
    eski=str(current_temperature-273)
    temp= { "Temperature" : eski }
    
    return json.dumps(temp)



    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

	



    