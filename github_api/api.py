import urllib.request as requests
import json

print("Welcome to Github User Activity Tracker")
username = input("Enter your username\n")

try:
    response = requests.urlopen(url= f"https://api.github.com/users/{username}/events")
    data = json.load(response)
    messages = [i['payload']['commits'][0]['message']for i in data[:3]]
except:
    print('Sorry Try again Later')
else:
    for i in messages:
        print(i)