import requests
import datetime
import csv

api_url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.weight:com.google.android.gms:merge_weight/datasets/0-1622803690000000000"

access_token = "ya29.a0AfH6SMBnbZt4Y4mYKjfrtWYVl14YUigQH8H3fQogCBlrbdX_VA5hUgzMWrv1A15dN9GnraG-lPt3NCRO_R1NowysUR3F2-SDijyxkTLt84RudJH-7HhKwjkinWjlhEGsX3TEnHE8PqE9KsemB7u_aBo1-l5O"

headers = {
    "Authorization": "Bearer {}".format(access_token),
    "Content-Type": "application/json;encoding=utf-8"
}

response = requests.get(api_url, headers=headers)

json_response = response.json()

point = json_response["point"]

ctr = 0

with open('weights.csv', mode='w', newline='') as csv_file:
	fieldnames = ['Date', 'Weight', 'BMI', 'Fat']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()

	for i in range(len(point)):
		weight = float(round(point[i]["value"][0]["fpVal"], 2))
		time_in_nanos = float(point[i]["startTimeNanos"])
		time_in_secs = time_in_nanos / 1e9
		dt = datetime.datetime.fromtimestamp(time_in_secs).strftime('%Y-%m-%d')
		writer.writerow({'Date': dt, 'Weight': weight, 'BMI': '0', 'Fat': '0'})
		ctr += 1	

print(f"There are {ctr} weigh-ins")
