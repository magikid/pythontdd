import datetime

'''

Here are the useful website: 
http://docs.python.org/library/unittest.html?highlight=unittest#basic-example
http://onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html

'''

class worktoday():

    def __init__(self, date, shift):
        '''
        date should be a datetime.date(year, month, day)
        shift should be either a, b, c, d
        '''
        
        self.date = date.isocalendar()
        self.day = date.isocalendar()[2]
        self.week = date.isocalendar()[1]
        self.shift = shift[0]

    def working(self):
        '''
        Work schedule is WW OO WWW, OO WW OOO
        '''
        
        if self.shift == "a" or self.shift == "b":        
            if(self.week % 2 == 0):
                if(self.day == 3 or self.day == 4):
                    return False
                else:
                    return True
            else:
                if(self.day == 3 or self.day == 4):
                    return True
                else:
                    return False
        elif self.shift == "c" or self.shift == "d":
            if(self.week % 2 == 0):
                if(self.day == 3 or self.day == 4):
                    return True
                else:
                    return False
            else:
                if(self.day == 3 or self.day == 4):
                    return False
                else:
                    return True