# python 2
#
# Problem Set 1, Problem 1: Dates
#
# Name:
#
import random
import time

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False


    def copy(self):
        """ Return a date object that is the same as the date in reference
        """
        return Date(self.month,self.day,self.year)

    def equals(self, d2):
        """ return if date object d2 == this date
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def tomorrow(self):
        """make the day tomorrow. also prints the new day for testing purposes
        """
        MDays = [31,28 + self.isLeapYear(),31,30,31,30,31,31,30,31,30,31]
        if self.day < MDays[self.month-1]:
            self.day += 1
        elif self.day == MDays[self.month-1] and self.month < 12:
            self.day = 1
            self.month += 1
        else:
            self.year += 1
            self.month = 1
            self.day = 1

    def yesterday(self):
        """make the day yesterday. also prints the new day for testing purposes
        """
        MDays = [31,28 + self.isLeapYear(),31,30,31,30,31,31,30,31,30,31]
        if self.day != 1:
            self.day -= 1
        elif self.day == 1 and self.month > 1:
            self.day =  MDays[self.month-2]
            self.month -= 1
        else:
            self.day = MDays[11]
            self.month = 12
            self.year -= 1

    def addNDays(self, N):
        """add n days
        """
        for i in range(0,N):
            self.tomorrow()

    def subNDays(self, N):
        """sub n days"""
        for i in range(0,N):
            self.yesterday()

    def isBefore(self, d2):
        """returns if d2 before self object"""
        if self.year != d2.year:
            return self.year < d2.year
        elif self.month != d2.month:
            return self.month < d2.month
        elif self.day != d2.day:
            return self.day < d2.day
        else:
            return False


    def isAfter(self, d2):
        """returns if d2 after self object"""
        if self.year != d2.year:
            return self.year > d2.year
        elif self.month != d2.month:
            return self.month > d2.month
        elif self.day != d2.day:
            return self.day > d2.day
        else:
            return False

    def daysInMonth(self,year,month):
        MDays = [31,28 + Date(1,1,year).isLeapYear(),31,30,31,30,31,31,30,31,30,31]
        return MDays[month-1]

    def diff(self, d2):
        """ counts dates between efficiently and stubbornly
        """
        if self.isBefore(d2):
            start = self
            end = d2
        else:
            start = d2
            end = self
        if self.equals(d2):
            return 0
        elif start.month == end.month and start.year == end.year:
            x = end.day - start.day
        elif start.year == end.year:
            #count to end of month
            x = self.daysInMonth(start.year,start.month) - start.day
            #count months between
            for i in range(start.month + 1, end.month):
                x += self.daysInMonth(start.year, i)
            #count to end day
            x += end.day
        else:
            #count to end of month
            x = self.daysInMonth(start.year,start.month) - start.day
            #count to end of year
            for i in range(start.month+1, 13):
                x += self.daysInMonth(start.year,i)
            #count years inbetween dates
            for i in range(start.year+1, end.year):
                x += 366 if Date(1,1,i).isLeapYear() else 365
            #count months in that year
            for i in range(1,end.month):
                x += self.daysInMonth(end.year, i)
            #count days in that month
            x += end.day

        return x if self.isBefore(d2) else -x

    def diffEasy(self, d2):
        """Loops until days are equal
        """
        start = self if self.isBefore(d2) else d2
        end = d2 if self.isBefore(d2) else self
        x=0
        while(start.isBefore(end)):
            start.tomorrow()
            x += 1
        if self.isAfter(d2) == True:
            x = -x
        return x

    def dow(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
        return days[Date(3,6,2016).diff(self)%7-1]

start = Date(12, 1, 2015)

end = Date(3,15,2016)
print end.diff(start)