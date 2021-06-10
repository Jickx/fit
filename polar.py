


# import requests

# url = 'https://polarremote.com/v2/oauth2/token?grant_type=authorization_code&code=ccab46efe7220f5708cf19dda755f035'
# headers = {
#     'Authorization': 'Basic YTA5NmQ0MTMtMTcxNy00ZmY3LWIyODAtZTg0OWVkZmYwY2ZkOjE3M2M2ZjhhLWMyZTYtNDViOS1iZTdkLTBiZTYzODMwZDViMg==',
#     'Content-Type': 'application/json',
#     'Accept': 'application/json;charset=UTF-8'
# }
# r = requests.post(url, headers = headers)

# print(r.url)
# print(r)
# print(r.text)



import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 3445300af9d561ae3a9d93ccc77327e8'
}

r = requests.get('https://www.polaraccesslink.com/v3/users/52498177', params={

}, headers = headers)

print(r.json())