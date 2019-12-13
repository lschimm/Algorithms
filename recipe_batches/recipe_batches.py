#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Plan 1
  # We'll have to compare two dictionaries to each other
  # Compare the first dictionary's values (the recipe) to the second (ingredients)
  # So loop through it once to see if there's enough (subtract the recipe from the ingredients)
  # if so, loop again to see if there's enough remainding for other batches
  # if not, then stop looping and return the amount available



  pass



  


  



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))