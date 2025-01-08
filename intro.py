# Importing dependencies
from flask import Flask, render_template, abort, request, jsonify
import os

#Declaring the app and where the folders and files are 
app = Flask(__name__, static_folder='static')

""" This is made up weather in json, and i use it to fetch from this memory and I'll post, update and delete from frontend """
weather_today = [
    {"id": 1, "city": "Berlin", "temperature": "17°C", "condition": "Overcast"},
    {"id": 2, "city": "Toronto", "temperature": "12°C", "condition": "Windy"},
    {"id": 3, "city": "Mumbai", "temperature": "30°C", "condition": "Humid"},
    {"id": 4, "city": "Rome", "temperature": "21°C", "condition": "Sunny"},
    {"id": 5, "city": "Shanghai", "temperature": "19°C", "condition": "Foggy"},
    {"id": 6, "city": "Dubai", "temperature": "35°C", "condition": "Hot"},
    {"id": 7, "city": "Moscow", "temperature": "10°C", "condition": "Snowy"},
    {"id": 8, "city": "Cape Town", "temperature": "23°C", "condition": "Breezy"},
    {"id": 9, "city": "Seoul", "temperature": "14°C", "condition": "Rainy"},
    {"id": 10, "city": "Los Angeles", "temperature": "28°C", "condition": "Clear"}
]


#Holidays in different countries
holiday_data = [
  {
    "id": 1,
    "country": "United States",
    "code": "US",
    "holidays": [
      {
        "id": "1a",
        "name": "New Year's Day",
        "date": "2023-01-01",
        "type": "National holiday"
      },
      {
        "id": "1b",
        "name": "Independence Day",
        "date": "2023-07-04",
        "type": "National holiday"
      },
      {
        "id": "1c",
        "name": "Thanksgiving Day",
        "date": "2023-11-23",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 2,
    "country": "Canada",
    "code": "CA",
    "holidays": [
      {
        "id": "2a",
        "name": "Canada Day",
        "date": "2023-07-01",
        "type": "National holiday"
      },
      {
        "id": "2b",
        "name": "Victoria Day",
        "date": "2023-05-22",
        "type": "Public holiday"
      },
      {
        "id": "2c",
        "name": "Thanksgiving",
        "date": "2023-10-09",
        "type": "Public holiday"
      }
    ]
  },
  {
    "id": 3,
    "country": "United Kingdom",
    "code": "GB",
    "holidays": [
      {
        "id": "3a",
        "name": "New Year's Day",
        "date": "2023-01-01",
        "type": "National holiday"
      },
      {
        "id": "3b",
        "name": "Christmas Day",
        "date": "2023-12-25",
        "type": "National holiday"
      },
      {
        "id": "3c",
        "name": "Boxing Day",
        "date": "2023-12-26",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 4,
    "country": "Australia",
    "code": "AU",
    "holidays": [
      {
        "id": "4a",
        "name": "Australia Day",
        "date": "2023-01-26",
        "type": "National holiday"
      },
      {
        "id": "4b",
        "name": "ANZAC Day",
        "date": "2023-04-25",
        "type": "National holiday"
      },
      {
        "id": "4c",
        "name": "Christmas Day",
        "date": "2023-12-25",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 5,
    "country": "India",
    "code": "IN",
    "holidays": [
      {
        "id": "5a",
        "name": "Republic Day",
        "date": "2023-01-26",
        "type": "National holiday"
      },
      {
        "id": "5b",
        "name": "Independence Day",
        "date": "2023-08-15",
        "type": "National holiday"
      },
      {
        "id": "5c",
        "name": "Gandhi Jayanti",
        "date": "2023-10-02",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 6,
    "country": "Germany",
    "code": "DE",
    "holidays": [
      {
        "id": "6a",
        "name": "German Unity Day",
        "date": "2023-10-03",
        "type": "National holiday"
      },
      {
        "id": "6b",
        "name": "Christmas Day",
        "date": "2023-12-25",
        "type": "National holiday"
      },
      {
        "id": "6c",
        "name": "New Year's Day",
        "date": "2023-01-01",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 7,
    "country": "Japan",
    "code": "JP",
    "holidays": [
      {
        "id": "7a",
        "name": "New Year's Day",
        "date": "2023-01-01",
        "type": "National holiday"
      },
      {
        "id": "7b",
        "name": "Coming of Age Day",
        "date": "2023-01-09",
        "type": "National holiday"
      },
      {
        "id": "7c",
        "name": "Emperor's Birthday",
        "date": "2023-02-23",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 8,
    "country": "France",
    "code": "FR",
    "holidays": [
      {
        "id": "8a",
        "name": "Bastille Day",
        "date": "2023-07-14",
        "type": "National holiday"
      },
      {
        "id": "8b",
        "name": "Christmas Day",
        "date": "2023-12-25",
        "type": "National holiday"
      },
      {
        "id": "8c",
        "name": "New Year's Day",
        "date": "2023-01-01",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 9,
    "country": "Brazil",
    "code": "BR",
    "holidays": [
      {
        "id": "9a",
        "name": "Carnival",
        "date": "2023-02-21",
        "type": "National holiday"
      },
      {
        "id": "9b",
        "name": "Independence Day",
        "date": "2023-09-07",
        "type": "National holiday"
      },
      {
        "id": "9c",
        "name": "Christmas Day",
        "date": "2023-12-25",
        "type": "National holiday"
      }
    ]
  },
  {
    "id": 10,
    "country": "South Africa",
    "code": "ZA",
    "holidays": [
      {
        "id": "10a",
        "name": "Freedom Day",
        "date": "2023-04-27",
        "type": "National holiday"
      },
      {
        "id": "10b",
        "name": "Heritage Day",
        "date": "2023-09-24",
        "type": "National holiday"
      },
      {
        "id": "10c",
        "name": "Christmas Day",
        "date": "2023-12-25",
        "type": "National holiday"
      }
    ]
  }
]

#Home page rendering
@app.route('/')
def home():
    return render_template("home.html")



#App route for weather template
@app.route('/weather')
def weth():
  return render_template('weather.html')


#weather app api 
@app.route('/api/weather', methods=['GET'])
def get_cit():
  city_name = request.args.get('city')
  if city_name:
    city = next ((item for item in weather_today if item['city'] == city_name.lower()),None)
    return jsonify(weather_today)

    if city:
      return jsonify(city)
    else:
      return jsonify({'error': 'City not found'}), 404
  else:
    return jsonify(weather_today)


''''
Build funtion to get a specific city weather, then give that id some logic so the user can update, and delete. Writte the logic to iterate new cities in a variable when the user creates a new city. Then create a new dictionary representing the weather data for the new city based on the data received in the request. And finnaly give the new city a unique id (new id function or assignt to variable so the new city can have new id) and add it into memory variable.
'''

#city id function
def get_specific_city(city_id):
    return next((item for item in weather_today if item['id'] == city_id),None)


#Get specific city by it's id 
@app.route('/api/weather/<int:city_id>', methods=['GET'])
def get_specific(city_id):
    city = get_specific_city(city_id)
    if city is None:
        abort(404, description='City not found')
    return jsonify(city), 200


#Post new city, create new_id and new_city dictionary and finnaly add it in to memory store
@app.route('/api/weather', methods=['POST'])
def post_city():
    if not request.json or not all(key in request.json for key in ["city", "temperature", "condition"]):
        abort(400, description='Invalid request: Missing required fields')
        return

        #generate new id
    new_id = max(item['id'] for item in weather_today) + 1 if weather_today else 1

    #create new_city dictionary

    new_city = {
        'id': new_id,
        'city': request.json['city'],
        'temperature': request.json['temperature'],
        'condition': request.json['condition']
    }

    #add in-memory list
    weather_today.append(new_city)

    return jsonify(new_city), 201


#Update current city using it's id
@app.route('/api/weather/<int:city_id>', methods=['PUT'])
def update_weather(city_id):
  global weather_today
  city = get_specific_city(city_id)
  if city is None:
    abort(404, description="City not found")
    
  if not request.json:
    abort(400, description="Invalid request: No data provided")

  #Update the city
  city['city'] = request.json.get('city', city['city'])
  city['temperature'] = request.json.get('temperature', city['temperature'])
  city['condition'] = request.json.get('condition', city['condition'])
    

  return jsonify(city), 200


#Delete specific city
@app.route('/api/weather/<city_id>', methods=['DELETE'])
def delete_city(city_id):
  city = get_specific_city(city_id)
  if city is None:
    abort(404, 'City not Found')

  weather_today = [item for item in weather_today if item['id'] != city_id]
  return jsonify({"message": "Weather data deleted"}), 200



#App route for calender template
@app.route('/calender')
def calen():
    return render_template('calender.html')


#calender app api 
@app.route('/api/calender', methods=['GET'])
def get_weather():
    return jsonify(holiday_data) 



if __name__ == '__main__':
    app.run(debug=True)