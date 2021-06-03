import json
import requests

api_url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"

access_token = "ya29.a0AfH6SMAxstEWKJSjGjLDpfrQRpy4S9QOl49HZhOGW5Xm4DVI7zRfh5dNaerBA68ZyjJzKLahbzNsConGUgL_2YhEwPbkV_7coK33zHCqkGWC5F3VQJzw9g8nSgEVoJCiGSSwKMHIviZ0sehPN9xeYJHxEN1Q"

headers = {
  "Authorization": "Bearer {}".format(access_token),
  "Content-Type": "application/json;encoding=utf-8"
  }

body = {
  "aggregateBy": [{
    "dataTypeName": "com.google.weight",
    "dataSourceId": "raw:com.google.weight:com.picooc.international:Weight"
  }],
  "bucketByTime": { "durationMillis": 86400000 },
  "startTimeMillis": 1621655896231,
  "endTimeMillis": 1622655896231
}


response = requests.post(api_url, data=json.dumps(body), headers=headers)

print(response.text)