import requests

a=requests.get('https://www.angeltv.org/index.php?gmt=5.5')

print(a.text)