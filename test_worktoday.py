import unittest
import datetime
from worktoday import *

class WorkTodayTests(unittest.TestCase):
        
    def testWorking(self):
        d = datetime.date(2012, 10, 26)
        p = worktoday(d, "b")
        self.failUnless(d.isocalendar() == p.date)
    
    def testToday(self):
        p = worktoday(datetime.date(2012, 10, 26), "b")
        self.failIf(p.working())
        
    def testYesterday(self):
        p = worktoday(datetime.date(2012, 10, 25), "b")
        self.failUnless(p.working())
        
    def testWorkingOnNewYears(self):
        d = datetime.date(2013,1,1)
        p = worktoday(d, "b")
        self.failIf(p.working())
    
    def testWorkingNewYearsEve(self):
        d = datetime.date(2012, 12, 31)
        p = worktoday(d, "b")
        self.failIf(p.working())
        
    def testShiftWorkingBaker(self):
        p = worktoday(datetime.date.today(), "b")
        self.failIf(p.working())
        
    def testShiftWorkCharlie(self):
        p = worktoday(datetime.date.today(), "charlie")
        self.failUnless(p.working())
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()