import requests
url = "https://raw.githubusercontent.com/koki0702introducing-python/master/dummy_api/youtube_top_rated.json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t']
