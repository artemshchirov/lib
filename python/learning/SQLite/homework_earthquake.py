# API - Application Programming Interface
import requests
import sqlite3

database = 'earthquakes_db.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()


def main():
    """
    Search info about earthquakes with input parameters.
    Uses API from https://earthquake.usgs.gov/fdsnws/event/1/
    """

    start_time = input('Enter the start time. Example: 2021-05-19\n')
    end_time = input('Enter the end time. Example: 2021-06-21\n')
    latitude = input('Enter the latitude. Example: 32.79 (Haifa, Israel)\n')
    longtitude = input('Enter the longtitude. Example: 34.98\n')
    max_radius_km = input('Enter the max radius in km. Example: 500\n')
    min_magnitude = input('Enter the min magnitude. Example: 2\n')

    result = api_search(start_time, end_time, latitude, longtitude, max_radius_km, min_magnitude)

    save_earthquakes_to_database(database, result)

    print_results()

    conn.commit()
    conn.close()


def save_earthquakes_to_database(filename_db, data):
    """
    Create database, table and put results(data) inside
    """
    # create_query = "CREATE TABLE earthquakes (number INTEGER, place TEXT, magnitude REAL);"
    # cursor.execute(create_query)

    insert_query = "INSERT INTO earthquakes VALUES (?, ?, ?)"

    earthquakes = data['features']
    earthquakes_list = []
    for num, earthquake in enumerate(earthquakes, start=1):
        place = earthquake['properties']['place']
        mag = earthquake['properties']['mag']
        earthquakes_list.append((num, place, mag))

    cursor.executemany(insert_query, earthquakes_list)


def print_results():
    """
    Распечатывает инфу из бд
    """
    database = 'earthquakes_db.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    select_query = "SELECT * FROM earthquakes"
    cursor.execute(select_query)

    earthquakes = cursor.fetchall()

    [print(row) for row in earthquakes]


def api_search(starttime, endtime, latitude, longtitude, maxradiuskm, minmagnitude):
    """

    """
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
