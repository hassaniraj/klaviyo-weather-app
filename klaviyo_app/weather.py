import json
from datetime import date

import requests
from klaviyo_app import get_api_key

API_ENDPOINT = 'http://api.wunderground.com/api/{}/{}/q/{}.json'


def _query_api(features, query):
    """ Query the Wunderground API
    :param features: feature you would like to access
    :param query: The location you'd like to query
    :return: The json returned by the API
    """
    url = API_ENDPOINT.format(get_api_key(), features, query)
    data = requests.get(url)
    parsed_data = json.loads(data.text)
    return parsed_data


def get_curr_temp(location):
    """ Gets current temperature at given location
    :param location:  location of the weather
    :return: current temperature of the location
    """
    data = _query_api('conditions', location)
    curr_temp = data['current_observation']['temp_f']
    return float(curr_temp)


def get_avg_temp(location):
    """ Gets the average temperature at this time of the year for the given location
    :param location: location of the weather
    :return: average temp in F
    """

    today = date.today()
    query = 'history_%s%s%s' % (today.year, today.month, today.day)
    data = _query_api(query, location)
    print data
    meantemp = data['history']['dailysummary'][0]['meantempi']
    return int(meantemp)


def is_raining(location):
    """ Check if its raining
    :param location:location of the weather
    :return: check if its going to rain
    """
    data = _query_api('conditions', location)
    precip_today = data['current_observation']['precip_today_in']

    return '0.00' not in precip_today


def get_curr_weather(location):
    """ Get the current weather of the location
    :param location: location of the weather
    :return: get the current weather description in brief
    """
    data = _query_api('forecast', location)
    weather = data['forecast']['txt_forecast']['forecastday'][0]['fcttext']
    return weather

