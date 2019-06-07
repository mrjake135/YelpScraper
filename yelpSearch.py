import requests
import json

api_key = 'YOURAPIKEY'
headers = {'Authorization': 'Bearer %s' % api_key}
allCoordinates = []
url='https://api.yelp.com/v3/businesses/search'
for i in range(0,200,50):
    params = {'term':'restaurants','location':'33.775620,-84.396286','limit':50, 'offset':i, 'radius': 5000, 'open_now': True, 'price': '1'}
    req=requests.get(url, params=params, headers=headers)
    places_result = json.loads(req.text)
    print(places_result)
    for place in places_result['businesses']:
        lat = place['coordinates']['latitude']
        lng = place['coordinates']['longitude']
        coordinates = [lng,lat]
        allCoordinates.append(coordinates)

with open ('places.json', 'w') as f:
    json.dump(allCoordinates, f)
    print('Places saved')
