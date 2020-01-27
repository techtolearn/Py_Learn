# https://www.youtube.com/watch?v=9N6a-VLBa2I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=47

# Python Tutorial: Working with JSON Data using the json Module - JSON - JavaScript Object Notation
import json

with open('states.json') as f:
    data = json.load(f)

#read the json file
#for state in data['states']:
   # print(state)
    #print(state['name'],state['abbreviation'])

for state in data['states']:
    del state['area_codes']

#after deleting the area code, we are dumping json content new file

with open('new_states.json', 'w') as f:
    json.dump(data,f, indent=2)  #indent will align the file data to readable




