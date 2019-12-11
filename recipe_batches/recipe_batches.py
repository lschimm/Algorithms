#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Plan...
  # the recipe value should be lower than the ingredient value
  # if the ingredient value is higher = return how many batches can be mad
  # if the recipe value is higher = return 0 / no batches can be made


# loop through the dictionary
# check each key and value to what is needed
#   as long as that value is >= the number, continue
#   if the value is >=
  pass 



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))