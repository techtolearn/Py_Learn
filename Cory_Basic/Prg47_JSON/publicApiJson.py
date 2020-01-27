'''
https://www.youtube.com/watch?v=9N6a-VLBa2I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=47

Some what unable to web contents
'''
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/currencies?.tsrc=fin-srch") as response:
    source = response.read()

data = json.loads(source)
#print(json.dumps(data, indent=2))

print(len(data['list']['resource']))

