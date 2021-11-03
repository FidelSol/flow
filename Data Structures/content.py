'''

DUNDER METHODS
Card Deck

'''
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck)) # __len__
print(deck[0]) # __getitem__
from random import choice
print(choice(deck)) # __getitem__
print(deck[:3]) # __getitem__
print(deck[12::13]) # __getitem__

for card in reversed(deck): # __getitem__
    print(card)

print(Card('Q', 'hearts') in deck) # __contains__
# SORTING
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_hight(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_hight):
    print(card)

'''

VECTOR CLASS

'''

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

'''
An Array of Sequences

Container sequences:
list, tuple, collections.deque - can hold items of different types

Flat sequences:
str, bytes, byteaarray, memoryview, array.array - can hold items of one type

Mutable sequences:
list, bytearray, array.array, collections.deque, memoryview

Immutable sequences:
tuple, str, bytes

UML class diagram:
Container:      Sequence:       MutableSequence:
__contains__    __getitem__     __setitem__
                __contains__    __delitem__
Iterable:       __iter__        insert
__iter__        __reversed__    append
                index           reverse
Sized:          count           extend
__len__                         pop
                                remove
                                __iadd__

'''

# UNPACKING TUPLES
import os
_, filename = os.path.split('/home/Fidel/.ssh/idrsa.pub')

divmod(20, 8)
t = (20, 8)
divmod(*t)

a, b, *rest = range(5)
print(a, b, *rest)

a, *body, c, d = range(5)
print(a, *body, c, d)

metro_areas = [('Tokio', 'JP', 36, (35, 139)), ('NCR', 'IN', 37, (37, 115))]
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(latitude, longitude)

# NAMED TUPLE
City = collections.namedtuple('City', 'name country population coordinates')
tokio = City('Tokio', 'JP', 36, (35, 139))
print(tokio.coordinates)

print(City._fields) # _fields
LatLong = collections.namedtuple('LatLong', 'lat long')
delphi_data = ('NCR', 'IN', 21, LatLong(28, 77))
delphi = City._make(delphi_data) # _make
print(delphi._asdict()) # _asdict
for key, value in delphi._asdict().items(): # _asdict
    print(key + ':', value)

# SLICING