""" 
You are assigned to put some amount of boxes onto one truck. 
You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]:

    numberOfBoxes_i is the number of boxes of type i.
    numberOfUnitsPerBox_i is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

>>> input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
>>> output: 8

>>> input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
>>> output: 91

접근법:
unit이 큰 순서대로 정렬한 후 그리디로 접근
"""
from typing import List
import unittest

def maximum_units(box_types: List[List[int]], truck_size: int) -> int:
    if not box_types:
        return -1
    
    # unit이 큰 순서대로 정렬
    box_types.sort(key=lambda b: b[1], reverse=True)
    
    # 트럭에 실을 짐의 갯수 
    loads = 0

    for box, unit in box_types:
        if truck_size - box <= 0:
            loads += truck_size * unit 
            break
        
        else:
            loads += box * unit 
            truck_size -= box 
    
    return loads

class test(unittest.TestCase):

    boxes: List[List[int]]
    size: int 
    expect: int 

    def test_example_1(self):
        boxes = [[1,3],[2,2],[3,1]]
        size = 4
        expect = 8
        self.assertEqual(maximum_units(boxes, size), expect)
    
    def test_example_2(self):
        boxes = [[5,10],[2,5],[4,7],[3,9]]
        size = 10
        expect = 91
        self.assertEqual(maximum_units(boxes, size), expect)

if __name__ == '__main__':
    unittest.main()