import requests
import datetime as dt
from dateutil.relativedelta import relativedelta


flight_url = 'https://tequila-api.kiwi.com/v2/search'
flight_api = 'zuex8J4mbVqLsJkqVUiiC-dR6Rd4ofep'

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
date_6 = now + relativedelta(months=6)
date_6 = date_6.strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def get_flight_price(self, code):
        headers = {"apikey" : flight_api}

        query = {
            "fly_from":"LON", 
            "fly_to": code, 
            "date_from": date,
            "date_to": date_6,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
            }

        response = requests.get(url = flight_url, headers = headers, params=query)

        try:
            result = response.json()
            price = result["data"][0]["price"]
        except IndexError:
            print(f"No flights found for {code}.")
            return None

        return (f"From LON to {code} price is €{price}")



