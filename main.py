from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

flight_details = FlightSearch()
sheety_data = DataManager()
flight_price = FlightData()

sheety = sheety_data.get_data()
prices = sheety['prices']

for i in range(len(prices)):
    if prices[i]['iataCode'] == '':
        city_code = flight_details.get_code(prices[i]['city'])
        
        data = {
            "price":{
                'iataCode':city_code
            }
        }

        sheety_data.put_data(f"/{prices[i]['id']}", data)

    print(flight_price.get_flight_price(prices[i]['iataCode']))


