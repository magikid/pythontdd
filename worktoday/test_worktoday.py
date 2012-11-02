import unittest
import datetime
from worktoday import *

class WorkTodayTests(unittest.TestCase):
        
    def testWorking(self):
        d = datetime.date(2012, 10, 26)
        p = worktoday(d, "b")
        self.assertTrue(d.isocalendar() == p.date)
    
    def testToday(self):
        p = worktoday(datetime.date(2012, 10, 26), "b")
        self.assertFalse(p.working())
        
    def testYesterday(self):
        p = worktoday(datetime.date(2012, 10, 25), "b")
        self.assertTrue(p.working())
        
    def testWorkingOnNewYears(self):
        d = datetime.date(2013,1,1)
        p = worktoday(d, "b")
        self.assertFalse(p.working())
    
    def testWorkingNewYearsEve(self):
        d = datetime.date(2012, 12, 31)
        p = worktoday(d, "b")
        self.assertFalse(p.working())
        
    def testShiftWorkingBaker(self):
        p = worktoday(datetime.date(2012,11,1), "b")
        self.assertFalse(p.working())
        
    def testShiftWorkCharlie(self):
        p = worktoday(datetime.date(2012,11,1), "charlie")
        self.assertTrue(p.working())
        
    def testShiftWorkFailBaker(self):
        p = worktoday(datetime.date(2012,11,1), "baker")
        self.assertFalse(p.working())
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()