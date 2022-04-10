import requests


sheety_key = 'https://api.sheety.co/e0b549c88c27125867b1fda763c35410/flightDeals/prices'

class DataManager:
    
    def get_data(self):
        response = requests.get(sheety_key)
        result = response.json()
        return result

    def post_data(self, post_data):
        response = requests.post(url=sheety_key, json=post_data)
        return response.text

    def put_data(self, row_id, put_data):
        response = requests.put(url=sheety_key+row_id, json=put_data)
        return response.text

