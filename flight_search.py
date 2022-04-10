import requests

flight_url = 'https://tequila-api.kiwi.com/locations/query'
flight_api = 'zuex8J4mbVqLsJkqVUiiC-dR6Rd4ofep'

class FlightSearch:

    def get_code(self, city):
        headers = {"apikey" : flight_api}
        query = {"term":city, "location_types": "city"}
        response = requests.get(url = flight_url, headers = headers, params=query)
        result = response.json()
        code = result["locations"][0]["code"]
        return code


