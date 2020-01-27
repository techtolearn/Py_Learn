# https://www.youtube.com/watch?v=K8L6KVGG-7o&index=30&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
re Module - How to Write and Match Regular Expressions (Regex)
'''

import re

text_to_Search=''''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ * + ? { } [ ] \ | ( )

coreyms.com


321-555-4321
123.555.1234
123*555*1234

Mr. Satheesh
Mr Saty
Ms Divya

Mrs.Tanvi Satheesh

'''
sentence = 'Start a sentence and then bring it to an end'

#raw string is prfixed with r  not to handle \ slashes

print('\tTAB')
print(r'\tTAB')

print(text_to_Search[2:5])
#patteren = re.compile(r'abc')
#patteren = re.compile(r'coreyms\.com')
#patteren = re.compile(r'.\d') # it matches only numbers
#patteren = re.compile(r'\D')    # it matches only not digits
#patteren = re.compile(r'\w')   # it looks of [a-z][A-Z][0-9]
#patteren = re.compile(r'\bHa')  # it matches word boundry
#patteren = re.compile(r'\BHa')

#patteren = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  or re.complie(r'\d{3}.\d{3}.d{4}')
# patteren = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# #patteren = re.compile(r'\BHa')
#
# matches = patteren.finditer(text_to_Search)    ##use patteren.findall(text_to_Search)
#
# for match in matches:
#     print(match)

urls ='''
https://www.google.com
http://coreyms.com
https://youtube.com
http://www.nas.gov
'''
#? says yes or no, () grouping
patteren = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = patteren.finditer(urls)

for match in matches:
    # print(match.group(0))
    # print(match.group(1))
    # print(match.group(2))
    print(match.group(3))

print("\n")
# we can also print the url based group number  - here 4 groups ()
patteren = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_url = patteren.sub(r'\2\3',urls)
print(subbed_url)

# search patteren by ignoring case
patteren = re.compile(r'start', re.I)
matches = patteren.search(sentence)
print(matches)
