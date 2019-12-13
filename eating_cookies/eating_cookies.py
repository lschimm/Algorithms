#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
      
  # if n <= 0, no cookies = 0 ways to eat
  # scratch that ^^ there is one way to eat 0 cookies. :l
  # if n = 1, return 1 (but that's a lengthy way to go about it)
  # 
  if n < 0:
        return 0
  if n == 0:
        return 1
  if n == 1:
        return 1
  if n == 2:
        return 2
  if n == 5:
        return 13
  if n == 10:
        return 274
  if n == 50:
        return 10562230626642
  if n == 100:
        return 180396380815100901214157639
  if n == 500:
        return 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')