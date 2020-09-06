# ac16ae04df4fd6e72f2231739d630dc9
# https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=439d4b804bc8187953eb36d2a8c26a02
from pprint import pprint
import requests
main_link = 'https://api.openweathermap.org/data/2.5/weather'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
           'Accept':'*/*'}
params = {'q':'Irkutsk',
          'appid':'ac16ae04df4fd6e72f2231739d630dc9'}
response = requests.get(main_link, headers=headers, params=params)
pprint(response.json())