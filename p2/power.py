"""
Power Hungry
============
Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen has been assigned to repair the solar panels, but you can't take them all down at once without shutting down the space station (and all those pesky life support systems!). 
You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".
Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the answer as a string representation of the number.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int list) xs = [2, 0, 2, 2, 0]
Output:
    (string) "8"
Inputs:
    (int list) xs = [-2, -3, 4, -5]
Output:
    (string) "60"
"""
from typing import List

def solution(xs: List[int]) -> int:
  """
  Recursive solution.
  """
  n = len(xs)
  if n <= 2:
    return max(xs)

  # to take care of edge cases
  count_pos, count_neg = 0, 0

  prod = 1
  for num in xs:
    if num != 0:
      prod *= num
      if num > 0:
        count_pos += 1
        continue
      count_neg += 1
  
  if count_pos == 0 and count_neg <= 1:
    return 0
  
  if prod < 0:
    greatest_neg = max([neg for neg in xs if neg < 0])
    prod //= greatest_neg

  return prod

if __name__ == "__main__":
  l1 = [2, -3, 1, 0, -5]
  l2 = [2, 0, 2, 2, 0]
  l3 = [-2, -3, 4, -5]
  print("l1: ", solution(l1))
  print("l2: ", solution(l2))
  print("l3: ", solution(l3))
