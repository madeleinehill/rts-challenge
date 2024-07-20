from typing import List

class Challenge:
  def aboveBelow(items: List[int], pivot: int):
    res = { 'above': 0, 'below': 0 }
    for num in items:
      if num > pivot:
        res['above'] += 1
      elif num < pivot: 
        res['below'] += 1

    return res
  
  def stringRotation(inputString: str, rotation: int):
    if rotation >= len(inputString):
      rotation = rotation % len(inputString)
    
    return inputString[-rotation:]+inputString[:-rotation]



test_case = [[1, 5, 2, 1, 10], 6]
print ('Running test case for aboveBelow:')
print(f'Input: {test_case[0]}, {test_case[1]}')
print("Output: " + str(Challenge.aboveBelow(test_case[0],test_case[1])))

test_case = ["MyString", 2]
print ('Running test case for stringRotation:')
print(f'Input: {test_case[0]}, {test_case[1]}')
print("Output: " + str(Challenge.stringRotation(test_case[0],test_case[1])))