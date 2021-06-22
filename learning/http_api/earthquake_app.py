# API - Application Programming Interface
import requests


def main():
    """
    Search info about earthquakes with input parameters.
    Uses API from https://earthquake.usgs.gov/fdsnws/event/1/
    """
    start_time = input('Enter the start time. Example: 2021-05-19\n')
    end_time = input('Enter the end time. Example: 2021-06-21\n')
    latitude = input('Enter the latitude. Example: 32.79\n')  # Haifa, Israel
    longtitude = input('Enter the longtitude. Example: 34.98\n')
    max_radius_km = input('Enter the max radius in km. Example: 500\n')
    min_magnitude = input('Enter the min magnitude. Example: 2\n')

    result = api_search(start_time,
                        end_time,
                        latitude,
                        longtitude,
                        max_radius_km,
                        min_magnitude)

    print_results(result)


def print_results(data):
    earthquake_list = data['features']
    for index, earthquake in enumerate(earthquake_list, start=1):
        place = earthquake['properties']['place']
        mag = earthquake['properties']['mag']
        print(f'{index}. Place: {place}. Magnitude: {mag}')


def api_search(starttime, endtime,
               latitude, longtitude,
               maxradiuskm,
               minmagnitude):

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
    response = requests.get(url, headers={'Accept': 'application/json'}, params={
        'format': 'geojson',
        'starttime': starttime,
        'endtime': endtime,
        'latitude': latitude,
        'longitude': longtitude,
        'maxradiuskm': maxradiuskm,
        'minmagnitude': minmagnitude
    })

    data = response.json()
    return data


if __name__ == '__main__':
    main()
