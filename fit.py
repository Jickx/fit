import json
import requests

api_url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/raw:com.google.weight:com.picooc.international:/datasets/0-1622730223497000000"

access_token = "ya29.a0AfH6SMDl51guxlitl6JrQXqthtUphUJ3BqnIlKaBT-RGtGxR4C-TQ8zn94qSAf0tKxzcAw1eiroII9TqvkyNYrPSyT79r5e90o_n4vqmSwlXW7kS-mV7fnV1ezvab8bR3btQQq3X-bSwDMBbegusB0P3lmv9"

headers = {
  "Authorization": "Bearer {}".format(access_token),
  "Content-Type": "application/json;encoding=utf-8"
  }

response = requests.get(api_url, headers=headers)



print(response.text)