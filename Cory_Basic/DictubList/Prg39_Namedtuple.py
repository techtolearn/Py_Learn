# https://www.youtube.com/watch?v=GfxJYp9_nJA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=39
'''
Python Tutorial: Namedtuple - When and why should you use namedtuples?
'''

from collections import namedtuple

Color = namedtuple('color',['red','green','blue'])

color = Color(2,3,5)

print(color.red)
print(color.green)

white = Color(6,7,8)
print(white.green)
