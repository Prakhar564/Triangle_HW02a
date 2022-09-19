

import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
    
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 is a Isosceles triangle')
    
    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isosceles','4,4,5 is a Isosceles triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(10,11,12),'Scalene','10,11,12 is a Scalene triangle')    


    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')    

    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is a equilateral triangle')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 is a equilateral triangle')

    def testInputsA(self):
      self.assertEqual(classifyTriangle(-2,-3,-4),'InvalidInput','Only positive values valid' )
    
    def testInputsB(self):
      self.assertEqual(classifyTriangle(-2,-3,-4),'InvalidInput','Only positive values valid' )

    def testInputsC(self):
      self.assertEqual(classifyTriangle(-2,-3,-4),'InvalidInput','Only positive values valid' )
    
    def testValidTriangles(self):
        self.assertEqual(classifyTriangle(4,4,199), 'Not A Triangle','4,4,199 is not a triangle')      
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

