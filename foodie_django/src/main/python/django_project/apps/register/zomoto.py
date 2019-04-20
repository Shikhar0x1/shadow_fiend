import json
import requests

#curl -X GET --header "Accept: application/json" --header "user-key: 9555d306a58a662bc6a5fe3b426bfbbb" "https://developers.zomato.com/api/v2.1/search?entity_id=21&entity_type=city&q=veg%20chow&sort=cost"

url = 'https://developers.zomato.com/api/v2.1/search?entity_id=21&entity_type=city&q=veg%20chow&sort=cost'
#payload = open("request.json")
# params = (
#     ('sort', 'cost'),
# )
headers = {"Accept": "application/json", "user-key": "9555d306a58a662bc6a5fe3b426bfbbb"}
r = requests.get(url, headers=headers)


print json.dumps(r)
