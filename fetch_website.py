import requests

link='https://palmuplife.com/'
response = requests.get(link)
print(response.status_code)