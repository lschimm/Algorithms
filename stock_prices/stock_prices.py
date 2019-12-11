#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # start price is 0
  # going through the list, picking the lowest number before highest number
  # subtracting those to find the highest profit
  # start_price = 0
  # max profit must be able to take negative numbers
# First try.
  max_profit = 0
  for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices) - 1):
              if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
  return max_profit

  # pass
                    

# print(find_max_profit([10, 7, 5, 8, 11, 9]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))